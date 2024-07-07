import json

with open("./data.json") as f:
    data = json.load(f)

channelId = data["channelId"]

def updateChannel(id):
    # sanitize
    castedId = int(id)

    global channelId
    channelId = castedId

    obj = {"channelId": castedId}

    with open("./data.json") as f:
        data = json.load(f)

    data.update(obj)
    with open("./data.json", "w") as f: # there's a w here but this code aint a w
            return json.dump(data, f, indent = 4)

# preserves counts when the bot is restarted
def updateCount(num):
    try:
        castedNum = int(num)
    except Exception:
        # yeah, so this can't parse math expressions quite yet, and I ***R.E.F.U.S.E*** to use eval, so I'll eventually make a custom parser
        resetCount()
        return False

    obj = {"currentCount": castedNum}

    with open("./data.json") as f:
        data = json.load(f)
    print(data)
    currentCount = data["currentCount"]

    if castedNum == currentCount + 1:
        data.update(obj)
        with open("./data.json", "w") as f:
            json.dump(data, f, indent = 4)
        return True
    else:
        resetCount()
        return False

def resetCount():
    with open("./data.json") as f:
        data = json.load(f)
    data.update({"currentCount": 0})
    with open("./data.json","w") as f:
        json.dump(data, f, indent = 4)