import json

with open("openstack.json", "r", encoding="utf8") as f:
    libreoffice_dict = json.load(f)

count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
for entry in libreoffice_dict:
        count2 += 1
        if(len(entry["reviewers"]) == 0):
            count3 +=1;
	if(len(entry["reviewers"]) == 0):
            count3 +=1;
	if(len(entry["reviewers"]) == 0):
            count3 +=1;
        if (len(entry["filePaths"]) == 0):
            count5 += 1;
            print(entry)
        if(entry["owner"]["name"] == ""):
            print (entry)
            count4 += 1
        if (entry["owner"]["accountId"] == None):
            print(entry)
            count4 += 1
        if (entry["timestamp"] == ""):
            print(entry)
            count4 += 1
        if (entry["changeNumber"] == None):
            print(entry)
            count4 += 1
        if (entry["changeId"] == ""):
            print(entry)
            count4 += 1
        for reviewer in entry["reviewers"]:
            count +=1
            if (reviewer["name"] == entry["owner"]["name"]):
                #print (entry)
                #print (entry["reviewers"])
                #print(entry["owner"]["name"])
                count1 += 1;

print("total number of reviewers: ",count)
print("total number of defects(same owner - same reviewer : ",count1)
print("total number of entries:", count2)
print("total number of defects (without reviewer):", count3)
print("total number of defects (without email and others):", count4)
print("total number of defects (without filepath):", count5)





