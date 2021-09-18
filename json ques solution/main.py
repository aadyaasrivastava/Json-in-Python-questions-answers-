# # Question 1
# # import json
# #
# # data = {"key1" : "value1", "key2" : "value2"}
# #
# # jsonData = json.dumps(data)
# # print(jsonData)
#
# #question 2
# # import json
# #
# # sampleJson = """{"key1": "value1", "key2": "value2"}"""
# #
# # data = json.loads(sampleJson)
# # print(data['key2'])
#
# #   Question 3
# # import json
# #
# # sampleJson = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
# # prettyPrintedJson  = json.dumps(sampleJson, indent=2, separators=(",", " = "))
# # print(prettyPrintedJson)
# #
# # #Question 4
# #
# # import json
# #
# # sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
# #
# # print("Started writing JSON data into a file")
# # with open("sampleJson.json", "w") as write_file:
# #     json.dump(sampleJson, write_file, indent=4, sort_keys=True)
# # print("Done writing JSON data into a file")
#
#
# #question 5
# #
# # import json
# #
# # sampleJson = """{
# #    "company":{
# #       "employee":{
# #          "name":"emma",
# #          "payble":{
# #             "salary":7000,
# #             "bonus":800
# #          }
# #       }
# #    }
# # }"""
# #
# # data = json.loads(sampleJson)
# # print(data['company']['employee']['payble']['salary'])
#
# # Question 6
# # import json
# # from json import JSONEncoder
# #
# # class Vehicle:
# #     def __init__(self, name, engine, price):
# #         self.name = name
# #         self.engine = engine
# #         self.price = price
# #
# # class VehicleEncoder(JSONEncoder):
# #         def default(self, o):
# #             return o.__dict__
#
# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
#
# print("Encode Vehicle Object into JSON")
# vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
# print(vehicleJson)


# Question 7
# import json
#
# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
# def vehicleDecoder(obj):
#         return Vehicle(obj['name'], obj['engine'], obj['price'])
#
# vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
#            object_hook=vehicleDecoder)
#
# print("Type of decoded object from JSON Data")
# print(type(vehicleObj))
# print("Vehicle Details")
# print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)


# Question 8
# part 1
# import json
#
# def validateJSON(jsonData):
#     try:
#         json.loads(jsonData)
#     except ValueError as err:
#         return False
#     return True
#
# InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
# isValid = validateJSON(InvalidJsonData)
#
# print("Given JSON string is Valid", isValid)


# Question 9
# import json
#
# sampleJson = """[
#    {
#       "id":1,
#       "name":"name1",
#       "color":[
#          "red",
#          "green"
#       ]
#    },
#    {
#       "id":2,
#       "name":"name2",
#       "color":[
#          "pink",
#          "yellow"
#       ]
#    }
# ]"""
#
# data = []
# try:
#     data = json.loads(sampleJson)
# except Exception as e:
#     print(e)
#
# dataList = [item.get('name') for item in data]
# print(dataList)

