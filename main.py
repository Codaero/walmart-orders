import csv

finalList = []
with open("orders.txt", 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if "Unavailable" not in line]
    for line in lines:
        int1 = line.find("Substitutions")
        int2 = line.find("Weight-adjusted")
        int3 = line.find("Shopped")
        index = max(int1, int2, int3)

        temp = []
        temp.append(line[0:index])
        temp.append(line[line.rfind("Qty") + 4:line.rfind('$') - 1])
        temp.append(line[line.rfind("$") + 1:])
        temp.append(float(temp[-1]) / float(temp[-2]))

        finalList.append(temp)

with open('output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    for line in finalList:
        writer.writerow([line[0], '$' + str(line[-1]), line[1]])
