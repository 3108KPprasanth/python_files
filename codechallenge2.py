import pandas as pd

ven_cap = pd.read_csv("C:/Users/3108p/code_challenge/vendor-capacities.csv")

# inp_cap = pd.read_csv("C:/Users/3108p/code_challenge/input-capacities.csv")

inp_cap = pd.DataFrame()
n = int(input("Enter n: "))
pur = []
item = []
quan = []

for i in range(n):
    read = list(input().split(" "))
    pur.append(read[0])
    item.append(read[1])
    quan.append(read[2])
    
inp_cap["Purchase ID"] = pur
inp_cap["Item"] = item
inp_cap["Req. Quantity"] = quan

Pur = []
Item = []
req_quan = []
IsAvail = []
Vendor_ID = []
Total = []
Time = []

for i in range(inp_cap.shape[0]):
    
    mincost = 100000
    mintime = 1000
    isavail = "false"
    vendor = " "
    
    for j in range(ven_cap.shape[0]):   
        
        if inp_cap["Item"][i] == ven_cap["Item"][j]:
            
            if int(ven_cap["Default Quantity Limit in KG"][j]) >= int(inp_cap["Req. Quantity"][i]):
                
                cost = int(ven_cap["Cost Per KG"][j])*int(inp_cap["Req. Quantity"][i])
                
            else:
                
                additional = int(ven_cap["Cost Per KG"][j]) + int(ven_cap["Additional Cost Per KG"][j])
                addtocost = ((int(inp_cap["Req. Quantity"][i])-int(ven_cap["Default Quantity Limit in KG"][j])) * additional)
                cost = (int(ven_cap["Cost Per KG"][j]) * int(ven_cap["Default Quantity Limit in KG"][j])) + addtocost
            
            if cost < mincost: 
                mincost = cost
                mintime = ven_cap["Time to Deliver"][j]
                isavail = "true"
                vendor = ven_cap["Vendor"][j]
                    
            elif cost == mincost:
                    
                if ven_cap["Time to Deliver"][j] < mintime:
                        
                    mintime = ven_cap["Time to Deliver"][j]
                    isavail = "true"
                    vendor = ven_cap["Vendor"][j]
                
                    
    IsAvail.append(isavail)
    Vendor_ID.append(vendor)
    if mincost == 100000 and mintime == 1000:
        Total.append(0)
        Time.append(0)
    else:
        Total.append(mincost)
        Time.append(mintime)
    Pur.append(inp_cap["Purchase ID"][i])
    Item.append(inp_cap["Item"][i])
    req_quan.append(inp_cap["Req. Quantity"][i])
    
out_cap = pd.DataFrame(list(zip(Pur,Item,req_quan,IsAvail,Vendor_ID,Total,Time)),columns=["Purchase Id","Item","Quantity","IsAvail","Vendor","Total cost","Time"])
print(out_cap) 