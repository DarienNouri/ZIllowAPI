import json
from tabulate import tabulate
from devFile import DecodeUrl


def addLocations(link):
    with open('locationPresets', 'r') as f:
        presets = json.load(f)
    decoder = DecodeUrl(link)
    u = decoder.decode_url()
    filters = decoder.get_url_filters(u)
    location_dict = {u['searchQueryState']['usersSearchTerm']: filters}
    presets.append(location_dict)
    print(presets)
    with open('locationPresets.json', 'w') as f:
        json.dump(presets, f)


def makeSelection():
    with open('locationPresets', 'r') as f:
        presets = json.load(f)
    dataDict = {}

    table = []
    count = 0
    for i in presets:
        dataDict[count] = list(i.items())
        count += 1

    for key, value in dataDict.items():
        selections = (str(key) + ': ' + str(value[0][0]))
        table.append([str(key), str(value[0][0])])
    print(tabulate(table, headers=["Index", "City/State"]))
    print("Enter an index")
    selectedIndex = int(input())
    row = dataDict[selectedIndex]
    cityState = row[0]
    metrics = row[0][1]
    #decoder = DecodeUrl()
    #setFilters = decoder.set_url_filters(metrics)
    return row


