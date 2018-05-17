import random

def flip_coin():
    return random.random() > 0.5

def pr_mon():
    mon_head_count = 0
    mon_tail_count = 0
    tues_count = 0
    for i in range(1000):
        if flip_coin():
            mon_head_count += 1
        else:
            mon_tail_count += 1
            tues_count += 1
    mon_count = mon_head_count + mon_tail_count
    print("mon: {} tues: {}".format(mon_count, tues_count))        
    print("pr mon: {}".format(mon_count / (mon_count + tues_count)))
    print("pr mon and heads: {}".format(mon_head_count / (mon_count + tues_count)))
    print("pr mon given heads: {}".format(mon_head_count / mon_count))
    print("pr heads given monday: {}".format(mon_head_count / mon_count))
    print("pr heads given wakeup: {}".format(mon_head_count / (mon_count + tues_count)))

pr_mon()
