import time as t
functions={}
status={'first castle health':10,'first castle soldiers':[],'second castle health':10,'second castle soldiers':[]}
coin={'first':0,'second':0}
def get_status():
    return status
def teach(team_id,soldier_id):
    if team_id=='first' or team_id=='second':
        if soldier_id=='3' or soldier_id=='10':
            status[team_id+' castle soldiers'].append(int(soldier_id)-1,0)
            coin-=int(soldier_id)
            return True
    return False
def add_event(callback,event_id):
    functions[event_id]=callback
while True:
    coin['first']+=1
    coin['second']+=1
    t.sleep(1)
