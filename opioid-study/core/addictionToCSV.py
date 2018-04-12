import json
import re
import io

def addictionToCSV():
    data = json.load(open('data/Addiction.json'))
    csv = ""

    for group, topics in data.items():
        for topicId, title in topics[0].items():
            for comment in title[0]['comments']:
                for userId, comments in comment.items():
                    csv += userId
                    csv += "|"
                    csv += comments[0]['1_Text']
                    csv += "/002"

    csv = re.sub("|", "", csv)
    csv = re.sub("\n", "", csv)
    csv = re.sub("/002", "\n", csv)

    with io.open('data/AddictionC.csv', "w", encoding="utf-8") as f:
        f.write(csv)

    f.close()