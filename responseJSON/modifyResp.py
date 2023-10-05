import json
from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:



    


    if flow.request.pretty_url == "https://api.opayweb.com/api/home/account":


        thisthing = json.loads(flow.response.content)
       
        value1 = "50,000.00" 
        thisthing["data"]["availableBalance"]["value"] = value1
        thisthing["data"]["totalBalance"]["value"] = value1
        thisthing["data"]["walletAccount"]["balance"]["value"] = value1

        



        flow.response.content = json.dumps(thisthing, ensure_ascii=False).encode('utf8')
