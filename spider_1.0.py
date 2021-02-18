
import requests
import re
def fs(aaa):
    fast,slow=0,0
    while fast<len(aaa):
        if aaa[fast]==aaa[slow]:
            fast += 1
        else:
            slow+=1
            aaa[slow]=aaa[fast]
    return aaa[:slow-1]
while True:
    ans=input('输入网址')
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    a=requests.get(ans,headers=headers)
    b=a.text
    k=[]
    results=re.findall('/(10\..*?)\s',b)
    # print(len(results))
    for i in results:
        c=re.search('(10\..*?)"',i)
        # print(c.group(1))
        k.append(c.group(1))
    k=fs(k)
    print(k)
    
