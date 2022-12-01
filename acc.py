import json

lst = {}
jsonString = json.dumps(lst)
jsonFile = open("account.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
