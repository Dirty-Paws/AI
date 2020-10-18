from csv import reader
# open file in read mode

dictionary={
    "MamaLevel":[],
    "SuLevel":[],
    "IsikLevel":[],
    "SicaklikLevel":[],
    "UltraLevel":[]
}
with open('cokhosverioldu.csv', 'r') as read_obj:
    for row in read_obj:
            if "Isik" in row:
                dictionary["IsikLevel"].append(row.strip(':Isik seviyesi\n'))
                if "M" in read_obj.readline():
                    data=1
                    dictionary["MamaLevel"].append(data)
                else:
                    data=0
                    dictionary["MamaLevel"].append(data)
            if "Su" in row:
                dictionary["SuLevel"].append(row.strip(': Suyun Seviyesi\n'))
                if "celsi" in read_obj.readline():
                    dictionary["SicaklikLevel"].append(row.strip(' celsius\n'))

                if "cm" in read_obj.readline():
                    dictionary["UltraLevel"].append(row.strip(' cm\n'))

print(dictionary["IsikLevel"])
print(dictionary["MamaLevel"])
print(dictionary["SuLevel"])
print(dictionary["SicaklikLevel"])
print(dictionary["UltraLevel"])


