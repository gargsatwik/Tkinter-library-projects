import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

req = requests.get("https://opentdb.com/api.php", params=parameters)
req.raise_for_status()
question_data = req.json()["results"]
