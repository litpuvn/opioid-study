import json
import re
import io

def addictionToCSV(jsonf,csvf):
    data = json.load(open(jsonf))
    csv = ""

    for group, topics in data.items():
        for topicId, title in topics[0].items():
            for comment in title[0]['comments']:
                for userId, comments in comment.items():
                    for a,b in comments[0].items():
                        csv += userId
                        csv += "|"
                        csv += b[0]['1_text']
                        csv += "/002"

    csv = re.sub("|", "", csv)
    csv = re.sub("\n", "", csv)
    csv = re.sub("/002", "\n", csv)

    with io.open(csvf, "w", encoding="utf-8") as f:
        f.write(csv)

    f.close()