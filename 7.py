# TOPIC : DICTIONARY
# IT IS A KEY - VALUE PAIR AND CHANGABLE ,
# HERE WE USE FLOWER BRACKET OR FUNCTION dict()
birthday = {"nagraj": "25-08-2009",
           "karthikeya":"18-09-2010",
           "vani":"20-02-1984"}

meanings = {"bengalur": "chiken biryani",
            "mysore": "mysore pakh",
            "shivamogga":"fish fry"}
print(birthday)
print(meanings)

# accesing dictionary elements
# andre birthady anno dictionary ya nagraj anno key value yanu anta
print(birthday["nagraj"])
print(birthday.get("vani", "not found"))
# use get function to avoid key error , python asking that if vani is 
#  not present in dictionary what will i print so we give it to 
#print not found 


birthday["vikas"] = "19-3-2008"
print("adding vikas to list")
print(birthday)
print("updating....")
birthday["nagraj"] = "25-08-2007"
print(birthday)
#birthday.pop("nagraj")
#del birthday["nagraj"]
print(birthday)
x = birthday.pop("nagraj")
print(x) 
print(birthday.keys())
print(birthday.values())
print(birthday.items())

# updating dictionary with other dictionary
meanings.update(birthday) # meaning dictionary updated with birthday dictionary 
print(meanings)

d = {
    "efg": 23434,
    "raj": 2334311,
    "note": "list cant be created in tuple",
    "friends": ["nagraj", "vikas"],
    
}
print(d)

item1 = {"name":"milk",
         "weight":1,
         "price":"50"
}

item2 = {"name":"tea powder",
         "weight":10,
         "price":"99.7"}

item = (item1,item2)
print(item)

print(f"total weight: {item1['weight']} + {item2['weight']}   kg")
