# pybot-log: Flask REST + PSQL

``` docker-compose up -d```

# Endpoints

## /api/bots

``` python
{'creation_date': '2019-04-08T23:01:24.880394',
 'rpa_id': '5abcab29-5a3b-48d8-b1e3-86395279e5c7',
 'rpa_name': 'NewTestRobot001'}
```

- GET
- POST
- DELETE

## /api/logs

``` python
{'idx': 0,
 'log_id': 'fa8e0efa-6844-4219-8f9c-a02b2c3b13dc',
 'message': 'This is a test message',
 'rpa_id': '5abcab29-5a3b-48d8-b1e3-86395279e5c7',
 'tag': 'test',
 'timestamp': '2019-04-08T23:02:26.952311',
 'tz': 'EST'}
```


- GET
- POST
- DELETE
