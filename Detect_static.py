Msc_db={"+91-9443666583":"int" , "+91-9442476883":"st" , "+91-9446061192":"st" , "+91-9446061191":"st" ,"+91-9445792265":"st" ,"+91-9445792267":"st" ,"+91-9445792254":"st" ,"+91-9445792264":"st" ,"+91-9445791164":"int" ,"+91-9445792464":"int","+91-8939481729":"int" , "+91-8190046163":"st" , "+91-8966061192":"st" , "+91-8166061191":"st" ,"+91-8925792265":"st" ,"+91-8125792267":"st" ,"+91-8925792254":"st" ,"+91-8195792264":"st" ,"+91-8925792264":"int" ,"+91-8125792464":"int"}
Bsnl={"+91-9443666583":"st" , "+91-9442476883":"st" , "+91-9446061192":"st" , "+91-9446061191":"st" ,"+91-9445792265":"st" ,"+91-9445792267":"st" ,"+91-9445792254":"st" ,"+91-9445792264":"st" ,"+91-9445791164":"int" ,"+91-9445792464":"int" }
bsnl_int=[]
bsnl_st=[]
for key , value in Bsnl.items():
    if Bsnl[key] == "st":
        bsnl_st.append(key)
    elif Bsnl[key] == "int":
        bsnl_int.append(key)
    else:
        continue
msc_st=[]
msc_int=[]
for key , value in Msc_db.items():
    if Msc_db[key] == "st":
        msc_st.append(key)
    elif Msc_db[key] == "int":
        msc_int.append(key)
    else:
        continue
for i in msc_int:
    if i in Bsnl:
        if i not in bsnl_int :
            print("This number is Spoofed:",i)
        else:
            continue
