import json


def verifyStr(data: str, method: str):
    if method == "inpt1":
        if data.lower() == "ma" or data.lower() == "major":
            return -1
        elif data.lower() == "mi" or data.lower() == "minor":
            return 0
        elif data.lower() == "pa" or data.lower() == "patch":
            return 1
        elif data.lower() == "re" or data.lower() == "release":
            return 2

    elif method == "alpha":
        if data.lower() == "y" or data.lower() == "yes":
            return "alpha"
        elif data.lower() == "n" or data.lower() == "no":
            return 0

    elif method == "beta":
        if data.lower() == "y" or data.lower() == "yes":
            return "beta"
        elif data.lower() == "n" or data.lower() == "no":
            return 0
        
    elif method == "rc":
        if data.lower() == "y" or data.lower() == "yes":
            return "rc"
        elif data.lower() == "n" or data.lower() == "no":
            return 0

    else:
        raise ValueError("Argument of the verifyStr function is incorrect")

def stripData(data, sep: str, key: None|str = None):
    res = [i.strip() for i in data[key].split(sep)]
    if len(res) == 1:
        return res
    if len(res) > 1:
        strip = [i.strip() for i in res[1].split(".")]

        subRes = [res[0], strip[0], strip[1]]
        return subRes

def retStr(data: list):
    val = ""
    for i in range(len(data)):
        if i == 0:
            val = str(data[i]) + "."
        if i == 1:
            val += str(data[i]) + "."
        if i == 2:
            if len(data) == 3:
                val += str(data[i])
            else:
                val += str(data[i]) + "-"
        if i == 3:
            val += data[i] + "." + str(data[i + 1])
            break
    return val
    
def pullData(typeData: str = ""):
    with open('../package.json', 'r') as file:
        json_data = json.load(file)
        if typeData != "":
            return json_data[typeData]
        else:
            return json_data

def UpdateJson(data: str):

    with open('../package.json', 'r') as file:
        json_data = json.load(file)
        json_data["version"] = data
    with open("../package.json", 'w') as file:
        json.dump(json_data, file, indent=2)