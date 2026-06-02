import datetime
def start(nameid):
    starttime=datetime.datetime.now()
    print(nameid,starttime)
    from sql import absentandadd
    a=absentandadd(nameid,starttime)########addsql
    return a
def stop(nameid):
    stoptime=datetime.datetime.now()
    print(nameid,stoptime)
    from sql import taikin
    a=taikin(nameid,stoptime)
    return a