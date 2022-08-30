import random
import phonenumbers
from phonenumbers import carrier
lst=[]
lst1=[]
for i in range (50000):
    num = random.randint(6000000000,9999999999)
    lst.append(num)
print("Database:",lst)
db_1=lst.copy()
airtel=[]
jio=[]
bsnl=[]
vi=[]

for i in lst:
    if len(airtel)<10000:
        airtel.append(i)
    else:
        break
# print("Airtel:",airtel)
for j in lst[10001:]:
    if len(jio)<10000:
        jio.append(j)
    else:
        break
# print("Jio:",jio)
for k in lst[20001:]:
    if len(bsnl)<10000:
        bsnl.append(k)
    else:
        break
# print("Bsnl:",bsnl)
for l in lst[30001:]:
    if len(vi)<10000:
        vi.append(l)
    else:
        break
# print("Vi:",vi)
cl=airtel+jio+bsnl+vi
for i in cl:
    if i in lst:
        lst.remove(i)
    else:
        continue
# print("Spoofed:",lst)
k=sorted(db_1)
# print(db_1)
print("Caller ID" + "     " + "  Status"+"   "+"Carrier")
for i in range(0,len(k)):
    if k[i] in lst:
        number="+91-"+str(k[i])
        service_pro = phonenumbers.parse(number)
        print(k[i],"     ","Spoofed","   ","   ", carrier.name_for_number(service_pro,"en"))
    else:
        number = "+91-" + str(k[i])
        service_pro = phonenumbers.parse(number)
        print(k[i],"     ","No Spoof","   ","   ", carrier.name_for_number(service_pro,"en"))
