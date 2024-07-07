import json

def updateJSON(guildId, channelId):
    # we *should* have also done this in the actual command file
    # but like...lets be safe
    channelId = int(channelId)

    # currently, guildId is useless
    # but it exists if we wish to expand this bot to more servers
    obj = {"guildId": guildId, "channelId": channelId}

    with open("./data.json") as f:
        data = json.load(f)

    data.update(obj)
    with open("./data.json", "w") as f: # there's a w here but this code aint a w
            return json.dump(data, f, indent = 4)