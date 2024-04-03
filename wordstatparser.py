import json, urllib.request, urllib.error
class WordstatParser:
    def __init__(self, url, token, username):
        self.url = url
        self.token = token
        self.username = username
        
        
    def getClientUnits(self):
        data = {
            'method': 'GetClientsUnits',
            'token': self.token,
            'param': [self.username]
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        request = urllib.request.urlopen(self.url,data) 
        response = json.loads(request.read().decode('utf8'))
        return response

    def createReport(self, phrases, geo = []):
        data = {
            'method': 'CreateNewForecast',
            'token': self.token,
            'param': {
                'Phrases': phrases,
                'GeoID': geo,
                "Currency": "RUB",
                }
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        request = urllib.request.urlopen(self.url,data) 
        response = json.loads(request.read().decode('utf8'))
        return response
    
    def getReportList (self):
        data = {
            'method': 'GetForecastList',
            'token': self.token    
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        request = urllib.request.urlopen(self.url,data) 
        response = json.loads(request.read().decode('utf8'))
        return response
        
    def readReport (self, reportID):
        data = {
            'method': 'GetForecast',
            'token': self.token,
            'param': reportID
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        request = urllib.request.urlopen(self.url,data) 
        response = json.loads(request.read().decode('utf8'))
        return response
    
    def deleteReport (self, reportID):
        data = {
            'method': 'DeleteForecastReport',
            'token': self.token,
            'param': reportID
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        request = urllib.request.urlopen(self.url,data) 
        response = json.loads(request.read().decode('utf8'))
        return response

    def saveReportToTxt (self, report, result, type_click):
        for i in range(len(report['data']['Phrases'])):
            phraseToReport = str(report['data']['Phrases'][i]['Phrase'])
            if type_click == '5':
                showsToReport = str(report['data']['Phrases'][i]['Clicks'])
            elif type_click == '9':
                showsToReport = str(report['data']['Phrases'][i]['FirstPlaceClicks'])
            else:
                showsToReport = str(report['data']['Phrases'][i]['PremiumClicks'])
            result.write(f'{phraseToReport}:{showsToReport}'+'\n')

        