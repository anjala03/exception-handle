import datetime
x= datetime.datetime.now()
print(x)
# to primt the year and day specoficlly
print(x.year)
print (x.strftime("%A"))
y= datetime.datetime(2024, 1, 12)
print(y)
#the concept of random
import random
a=random.random()
print(a)
lst= ["ram", "hari", "shyam"]
print(random.choice(lst))
#the concept of json-convert form json to python
import json
m= '{"name":"anjala", "age":30, "city": "abc"}'
n= json.loads(m)
print(n["name"])
#conversion from python to json
p= {"name":"Ajita", "age":22, "city": "Sydney"}
q= json.dumps(p)
print(q)


