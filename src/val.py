import json
import re

import requests



def getJson(username, tag, requestType):
    if requestType == "profile":
        url = f"https://tracker.gg/valorant/profile/riot/{username}%23{tag}/overview?season=all"
    else:
        url = f"https://tracker.gg/valorant/profile/riot/{username}%23{tag}/matches?season=all"

    r = requests.get(url)

    data = r.text.strip()
    print(data)

    regex = re.compile(r'(?<={"route").*(?=}}}})', flags=re.DOTALL)
    djson = regex.search(data).group()
    js = '{"route"%s}}}}' % djson

    js = js.replace(r"\\u002F", r"//")
    jsss = json.loads(js)

    return jsss
