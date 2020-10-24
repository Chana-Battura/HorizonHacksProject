import json
def give_data():
    animal = {'type':'cat', 'age':12}
    as_json = json.dumps(animal)

    return as_json
def add_db(data):
    ##LOAD INTO DATABASE
    print(data)
    print(type(data))
