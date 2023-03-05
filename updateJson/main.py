import json


def main():
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

    def stripData(data, sep: str, key: None|str = None, subStrip: 0 | 1 = 0):
        res = [i.strip() for i in data[key].split(sep)]
        if len(res) == 1:
            return res
        if len(res) > 1 or len(res) == 2 and subStrip == 1:
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
    
    with open('../package.json', 'r') as file:
        inpt = input("Major, Minor, Patch or Release (Ma, Mi, Pa, Re or full Length): ")
        inpt = verifyStr(inpt, "inpt1")

        if inpt != 2:
        
            inpt2 = input("Alpha(Yes or No | Y or N): ")

            inpt2 = "alpha" if verifyStr(inpt2, "alpha") == "alpha" else None

            if inpt2 == None:
                
                inpt2 = input("Beta(Yes or No | Y or N): ")
                inpt2 = "beta" if verifyStr(inpt2, "beta") == "beta" else None

                if inpt2 == None:
                    inpt2 = input("Release Candidate(Yes or No | Y or N): ")

                    inpt2 = "rc" if verifyStr(inpt2, "rc") == "rc" else None
        else:
            inpt2 = None
                

        json_data = json.load(file)
        item_additional = stripData(json_data, "-", "version", 1)
        item_val = [i.strip() for i in item_additional[0].split(".")]

        prevVal = ""

        if int(item_val[0]) == 0 and inpt2 != None or inpt2 != None:
            if inpt2 == "alpha":
                if len(item_additional) == 1:
                    item_additional.append("a")
                    item_additional.append(0)
                else:
                    prevVal = item_additional[1]
                    item_additional[1] = "a"

            elif inpt2 == "beta":
                if len(item_additional) == 1:
                    item_additional.append("b")
                    item_additional.append(0)
                else:
                    prevVal = item_additional[1]

                    if item_additional[1] == "a" or item_additional[1] == "rc":
                        item_additional[2] = 0

                    item_additional[1] = "b"
            
            elif inpt2 == "rc":
                if len(item_additional) == 1:
                    item_additional.append("rc")
                    item_additional.append(0)
                else:
                    prevVal = item_additional[1]

                    if item_additional[1] == "a" or item_additional[1] == "b":
                        item_additional[2] = 0

                    item_additional[1] = "rc"
        elif inpt2 == None:
            if len(item_additional) > 1:
                for i in range(len(item_additional)):
                    item_additional.pop()
                    if len(item_additional) == 1:
                        break

        #Indexes
        a = int(item_val[0])
        b = int(item_val[1])
        c = int(item_val[2])

        # a or b
        if len(item_additional) > 1:
            d = item_additional[1]
            # num
            e = int(item_additional[2]) + 1

        if len(item_additional) == 1:
            if inpt == -1:
                a += 1
                b = 0
                c = 0
            elif inpt == 0:
                b += 1
                c = 0
            elif inpt == 1:
                c += 1
            elif inpt == 2:
                a += 1
                b = 0
                c = 0

        else:
            if inpt == -1 and prevVal == e:
                a += 1
            elif inpt == 0 and prevVal == d:
                b += 1
            elif inpt == 1 and prevVal == d:
                c += 1
            
        fullStr = retStr([a, b, c, d, e]) if len(item_additional) > 1 else retStr([a, b, c])

        json_data["version"] = fullStr
    with open("../package.json", 'w') as file:
        json.dump(json_data, file, indent=2)


if __name__ == "__main__":
    main()