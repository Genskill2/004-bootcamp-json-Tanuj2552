# Add the functions in this file
import json

def load_journal(file_name):
    f = open(file_name,)
    data = json.load(f)
    return data

def compute_phi(file_name, event):
    data = load_journal(file_name)
    days = len(data)
    ev, sq = 0, 0
    n11, n00, n10, n01, n1_, n0_, n_1, n_0 = 0,0,0,0,0,0,0,0 
    for daily_events in data:
        ev, sq = 0, 0
        if event in daily_events['events']:
            ev = 1
            n1_ += 1
        else:
            n0_ += 1

        if daily_events['squirrel']:
            sq = 1
            n_1 += 1
        else:
            n_0 += 1
        
        if ev and sq:
            n11 += 1
        elif ev==1  and sq==0:
            n10 += 1
        elif ev==0 and sq==1:
            n01 += 1
        else:
            n00 += 1

    return (n11*n00 - n10*n01)/((n1_*n0_*n_0*n_1)**0.5)
           
def compute_correlations(file_name):
    data = load_journal(file_name)
    dict_events = {}
    for each_day in data:
        for each_event in each_day['events']:
            if(each_event not in dict_events.keys()):
                print(each_event)
                dict_events[each_event] = compute_phi(file_name, each_event)

    return dict_events

def diagnose(file_name):
    dict_events = compute_correlations(file_name)
    max_val, min_val = -2, 2
    max_event = []
    min_event = []
    for x in dict_events.keys():
        if(dict_events[x] > max_val):
            max_val = dict_events[x]
            max_event.append(x)
        if(dict_events[x] < min_val):
            min_val = dict_events[x]
            min_event.append(x)

    return max_event[-1], min_event[-1]

