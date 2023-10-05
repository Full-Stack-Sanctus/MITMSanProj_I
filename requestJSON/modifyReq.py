import json
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:



    


    if flow.request.pretty_url == "https://cardh5.opayweb.com/apiBuried/tracker/event/v2":


        thisthing = json.loads(flow.request.content)
       
        value1 = "+2347042420823" 
        thisthing["phoneNumber"] = value1

        



        flow.request.content = json.dumps(thisthing, ensure_ascii=False).encode('utf8')
