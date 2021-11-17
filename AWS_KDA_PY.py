

# Import 
import boto3 
import datetime 
import random 

STREAM_NAME = 'input-stream' 


# Generator 
def get_data():
    return {
        "event_time": datetime.datetime.now().isoformat(), 
        "ticker": random.choice(["AAPL", "AMZN", "MSFT", "INTC", "TBV"]), 
        "price": round(random.random() * 100,2)
    }

# Generate 
def generate(stream_name, kinesis_client):
    while True: 
        data = get_data() 
        print(data) 
        kinessis_client.put_record(
            StreamName = stream_name, 
            Data = json.dumps(data) , 
            PartitionKey = "partitionkey"
        )

# dadsadadd
if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client("kinesis"))

