import json

print(json.dumps({
    "name": "Freewind",
    "age": 1000
}))

print(json.loads('{"name": "Freewind", "age": 1000}'))
