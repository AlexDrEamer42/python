import requests,time

todate = int(time.time())
fromdate = todate - 2 * 24 * 60 * 60    
param = {"order":"desc","sort":"activity","site":"stackoverflow","tagged":"Python","fromdate":fromdate,"todate":todate}
resp = requests.get('https://api.stackexchange.com/2.3/questions/',params = param)
if resp.status_code == 200:
    questions = resp.json()['items']
    for question in questions:
        print (question['title'])  
else:
    print('Что-то пошло не так')

