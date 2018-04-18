import json
import re
import io

def degeneToCSV(jsonf,csvf):
    data2 = json.load(open(jsonf))
    csv2 = ""
    for user, com in data2.items():
        # print(user)
        for x, y in com[0].items():
            # print(x)
            # print(y)
            for a in y:
                for b in a.items():
                    for c in b[1]:
                        csv2 += user
                        csv2 += "|"
                        try:
                            csv2 += c['1_text']
                        except KeyError:
                            pass
                        csv2 += '/002'

    csv2 = re.sub("|", "", csv2)
    csv2 = re.sub("\n", "", csv2)
    csv2 = re.sub("/002", "\n", csv2)

    with io.open(csvf, "w", encoding="utf-8") as f:
        f.write(csv2)

    f.close()

#for filename in glob.glob('data/dataR/*.txt'):
 #   print(filename)
  #  jsonfile = os.path.splitext(filename)[0]
   # jsonfile = jsonfile.strip(" ")
    #print(jsonfile)
    #csvfile = jsonfile + '.csv'
    #csvfile = csvfile.strip(" ")
    #print(csvfile)

    #addictionToCSV(filename,csvfile)