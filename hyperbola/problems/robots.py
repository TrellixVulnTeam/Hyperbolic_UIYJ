import hyperbola
import requests
import re
@hyperbola.Commander.add_worker('url')
class Robots:
    async def return_solution(self, data):
        nurl = 'http://' + data.replace(r'([^/].*?)\/.*', '\1')
        newdata = []
        links = []
        try:
            req = requests.get(nurl)
            for i in re.findAll(r'[Aa]llow[ \t]*?:[ \t]*?(\S+)', req.text):
                links.append(nurl + i.groups(1))
            newdata.append(req.text)
        except: pass
        try:
            req = requests.post(nurl)
            newdata.append(req.text)
        except: pass
        return {'logs':[], 'newdata':[{'type':'text','data':i} for i in newdata] + [{'type':'url','data':i} for i in links], 'end':False}