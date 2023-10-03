#creation of the Python REST API using the Fastapi framework
from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from clickhouse_driver import Client
import os


app = FastAPI()

upload_dir = "upload"
clickhouse_client = Client('127.0.0.1:9000')  

#POST request being used as this is the script responsible for uploading the game_rounds.csv file
@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, file.filename)

    #snippet responsible for writing the csv file into the given directorly
    with open(file_path, 'wb') as csv_file:
        csv_file.write(file.file.read())
    
    #adding file size as an added measure to make sure that the entire file is being uploaded
    file_size = os.path.getsize(file_path)

    # Check if the file has been successfully saved
    if os.path.isfile(file_path):
        return {"message": "File uploaded successfully", 
                "file_name": file.filename, 
                "file_size": f"{file_size/ (1024*1024):.2f} MB"
                }
    else:
        raise HTTPException(status_code=500, detail="Failed to save the file")
    
#aggregation endpoint (get)

@app.get("/aggregates/")
async def get_aggregates(
    user_id: str = Query(..., description="Player ID"),
    game_id: int = Query(..., description="Game ID")
):
    try:
        # query ClickHouse for aggregates
        query = f"""
        SELECT
            hour,
            user_id,
            game_id,
            total_real_amount_bet,
            total_bonus_amount_bet,
            total_real_amount_win,
            total_bonus_amount_win
        FROM RIVER_TECH.hourly_aggregates
        WHERE user_id = {user_id}
            AND game_id = {game_id}
        ORDER BY hour;
        """

        result = clickhouse_client.execute(query)
        print(result)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


#setting up host and port for this api endpoint
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
