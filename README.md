# rivertech_jack_bugeja
# python version 3.10

1. Extract the gamerounds.tar.gz file using the following command:
tar -xzvf gamerounds.tar.gz

2. run the python script: app.py to start the REST api
python3.10 kafka_integration.py

3. run the following curl command to upload the gamerounds.csv using the POST method in app.py:
curl -X POST -F "file=@gamerounds.csv" http://localhost:8000/upload/

The file should be in in api/upload, and you should get a message from the REST api, as shown in the image below

![Screenshot 2023-10-01 at 10 40 02](https://github.com/Grampun/rivertech_jack_bugeja_submission/assets/29627317/f9eff0cf-6b59-4086-aa02-c7277fac50eb)

![Screenshot 2023-10-01 at 10 40 11](https://github.com/Grampun/rivertech_jack_bugeja_submission/assets/29627317/79bfd576-6c55-4bf1-a2e8-679a4bbd39ca)

4. make sure you have kafka and zookeeper installed on your system and that you have both instances running on your machine.
I have configured zookeeper & kafka to run on their default ports

5. create the following topic using the command:
kafka-topics --create --topic staging-bets --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

![Screenshot 2023-10-02 at 09 31 23](https://github.com/Grampun/rivertech_jack_bugeja_submission/assets/29627317/ac51a7fc-47b9-4784-b0ed-439a2d63b749)

6. run the kafka_integration.py:
python3.10 kafka_integration.py
