import uuid
import datetime
import json
import requests

def new_id():
    return str(uuid.uuid4())

def iso_now():
    return datetime.datetime.now().isoformat()

http_header = {
    'Content-type': 'application/json',
    'X-Secret-Key':'ACCESS_TOKEN'
    }

new_bot = {
    "rpa_id": new_id(),
    "rpa_name": "NewTestRobot001",
    "creation_date": iso_now()
}

r = requests.post(
    "http://localhost:3030/api/bots",
    data=json.dumps(new_bot),
    headers=http_header)

response_data = json.loads(r.content)
rpa_id = response_data["rpa_id"]


test_log_1 = {
    "rpa_id": rpa_id,
    "log_id": new_id(),
    "idx": 0,
    "message": "This is a test message",
    "tag": "test",
    "timestamp": iso_now(),
    "tz": "EST",
}

test_log_2 = {
    "rpa_id": rpa_id,
    "log_id": new_id(),
    "idx": 1,
    "message": "This is a test message",
    "tag": "test",
    "timestamp": iso_now(),
    "tz": "EST",
}

test_log_3 = {
    "rpa_id": rpa_id,
    "log_id": new_id(),
    "idx": 2,
    "message": "This is a test message",
    "tag": "test",
    "timestamp": iso_now(),
    "tz": "EST",
}

for log in [test_log_1, test_log_2, test_log_3]:
    r = requests.post(
        "http://localhost:3030/api/logs",
        data=json.dumps(log),
        headers=http_header
    )
    print(r)

for log in [test_log_1, test_log_2, test_log_3]:
    r = requests.delete("http://localhost:3030/api/logs/%s" % log["log_id"])
    print(r)

r = requests.delete("http://localhost:3030/api/bots/%s" % rpa_id)
print(r)