import json
import urllib.request
filename=str(input("dwse arxeio:"))
f = open(filename, "r")
f_data = f.read()
dict_js = json.loads(f_data)
print(dict_js)
kleidia = []
times = []
for i in dict_js.keys():
    kleidia.append(i)
for j in dict_js.values():
    times.append(j)
for i in range (len(kleidia)):
    sundesmos = "https://min-api.cryptocompare.com/data/pricemulti?fsyms="+kleidia[i]+"&tsyms=EUR&api_key=#dwse API"
    op=urllib.request.urlopen(sundesmos)
    keimeno=op.read()
    keimeno=keimeno.decode()
    dict_js = json.loads(keimeno)
    axia = dict_js[i]["EUR"]*times[i]
    print(axia,kleidia[i])
    print("H axia tou" + kleidia[i] + "einai"+ axia)
