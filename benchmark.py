import os, time, json, httpx
from dataclasses import dataclass, asdict
from dotenv import load_dotenv
load_dotenv()

TASKS=[
 {'name':'python_bugfix','prompt':'Fix bug: def add(a,b): return a-b. Return corrected code only.'},
 {'name':'regex_extract','prompt':'Write Python regex to extract emails from text. Include short explanation.'},
 {'name':'linux_debug','prompt':'Explain why disk is full and give safe cleanup commands for Ubuntu.'},
]

@dataclass
class Result: name:str; latency_ms:int; ok:bool; output:str

def call(prompt):
    url=os.getenv('MIMO_URL','https://platform.xiaomimimo.com/v1/chat/completions')
    key=os.getenv('MIMO_API_KEY','')
    body={'model':os.getenv('MIMO_MODEL','mimo-v2.5'),'messages':[{'role':'user','content':prompt}]}
    t=time.time(); r=httpx.post(url,headers={'Authorization':f'Bearer {key}'},json=body,timeout=120)
    ms=int((time.time()-t)*1000); data=r.json()
    out=data.get('choices',[{}])[0].get('message',{}).get('content',str(data))
    return ms,out

results=[]
for task in TASKS:
    ms,out=call(task['prompt'])
    results.append(Result(task['name'],ms,bool(out),out[:2000]))
print(json.dumps([asdict(r) for r in results],indent=2))
