from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer, AvroConsumer
from fastavro import writer, parse_schema
from api import app

import json

#importing the upload_dir variable from the app.py script

#kafka config
kafka_broker_url = 'localhost:9092'
schema_registry_url = 'http://0.0.0.0:8000/upload/'
#write to the following topic
kafka_topic = 'staging-bets'

#avro file in schema folder
avro_schema_file = 'schemas/game_rounds_schema.avsc'

with open(avro_schema_file, 'r') as schema_file:
    avro_schema = json.load(schema_file)

# kafka producer
producer = AvroProducer({
    'bootstrap.servers': kafka_broker_url,
    'schema.registry.url': schema_registry_url
})

consumer = AvroConsumer({
    'bootstrap.servers': kafka_broker_url,
    'group.id': 'game-rounds-group',
    'auto.offset.reset': 'earliest',
    'schema.registry.url': schema_registry_url
})

#convert csv to avro and send the payload to kafka
def send_data_to_kafka(csv_data):

    avro_data = [] 
    for row in csv_data:
        avro_record = {}

        avro_record['created_timestamp'] = row['created_timestamp']
        avro_record['game_instance_id'] = row['game_instance_id']
        avro_record['user_id'] = row['user_id']
        avro_record['game_id'] = row['game_id']
        avro_record['real_amount_bet'] = row['real_amount_bet']
        avro_record['bonus_amount_bet'] = row['bonus_amount_bet']
        avro_record['real_amount_win'] = row['real_amount_win']
        avro_record['bonus_amount_win'] = row['bonus_amount_win']
        avro_record['game_name'] = row['game_name']
        avro_record['provider'] = row['provider']

    #send avro to kafka
    for record in avro_data:
        print("record being pushed to producer " + record)
        producer.produce(topic=kafka_topic, value=record)

    producer.flush()

#convert csv records into a list of dictionaries
def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-16', errors='ignore') as csv_file:
        lines = csv_file.read().splitlines()
        print(lines[0:5])
        header = lines[0].split(',')
        data = [dict(zip(header, line.split(','))) for line in lines[1:]]
        # print(data[5])
    return data 


if __name__ == '__main__':
    csv_data = read_csv(app.upload_dir + '/gamerounds.csv')
    send_data_to_kafka(csv_data)

    consumer.subscribe([kafka_topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(msg.error())
            else:
                print(msg.value)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

