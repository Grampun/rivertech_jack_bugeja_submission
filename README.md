# rivertech_jack_bugeja
# python version 3.10.7

1. Extract the gamerounds.tar.gz file using the following command:
tar -xzvf gamerounds.tar.gz

2. run the python script: app.py to start the REST api
python3.10 kafka_integration.py

3. run the following curl command to upload the gamerounds.csv using the POST method in app.py:
curl -X POST -F "file=@gamerounds.csv" http://localhost:8000/upload/

The file should be in in api/upload, and you should get a message from the REST api, as shown in the image below

4. make sure you have kafka and zookeeper installed on your system and that you have both instances running on your machine.
I have configured zookeeper & kafka to run on their default ports

5. create the following topic using the command:
kafka-topics --create --topic staging-bets --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

6. run the kafka_integration.py:
python3.10 kafka_integration.py