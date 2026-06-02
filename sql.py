from sqlalchemy import Column, Integer, String,Boolean, create_engine ,ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import os
import datetime
from sqlalchemy import DateTime


Base = declarative_base()
engine = create_engine("sqlite:///kintai.db")

Session = sessionmaker(bind=engine)
session = Session()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    active = Column(Boolean, default=True)
    attendances = relationship("User", back_populates="rel1")

class User(Base):
    __tablename__ = 'kintai'

    id = Column(Integer, primary_key=True)
    nameid = Column(Integer, ForeignKey("employees.id"))
    workingtime = Column(Integer)
    starttime=Column(DateTime)
    finishtime=Column(DateTime)

    rel1=relationship("Employee", back_populates="attendances")
##############ファイルがなければ作成#######################################################################
######################################################################################################
fileexists=os.path.exists("C:/Users/chihi/OneDrive/デスクトップ/kintai/kintai.db")
if fileexists==False:
    Base.metadata.create_all(engine)
####################################################################################################
###############################################################################################

def addname(namee):
    session=Session()
    inp=namee
    emp = Employee(name=inp)
    session.add(emp)
    session.commit()


def emplistcheck():
    d = {}
    session=Session()
    records = session.query(Employee).all()
    for r in records:
        if r.active==True:
            d[r.id] = r.name
    return d

def firelistcheck():
    d = {}
    session=Session()
    records = session.query(Employee).all()
    for r in records:
        if r.active==False:
            d[r.id] = r.name
    return d

def add(nameid,starttime):
    session =Session()
    addrecord = User(
        nameid=nameid,
        starttime=starttime
    )

    session.add(addrecord)
    session.commit()


def absentandadd(nameid,starttime):
    session=Session()
    today = datetime.date.today()
    record = session.query(User).filter(
    User.nameid == nameid,
    User.finishtime == None,
    User.starttime >= datetime.datetime.combine(today, datetime.time.min),
    User.starttime <= datetime.datetime.combine(today, datetime.time.max)
    ).first()
    if record is None:
        bun="出勤開始します"
        print(bun)
        add(nameid,starttime)
        return bun
    else:
        bunb="出勤中です"
        print("出勤中です")
        return bunb
def taikin(nameid,stoptime):
    session=Session()
    today = datetime.date.today()
    record = session.query(User).filter(
    User.nameid == nameid,
    User.finishtime == None,
    User.starttime >= datetime.datetime.combine(today, datetime.time.min),
    User.starttime <= datetime.datetime.combine(today, datetime.time.max)
    ).first()
    if record and record.finishtime is None:
        print("退勤します")
        bun="退勤します"
        record.finishtime = stoptime
        session.commit()
        return bun
    else:
        print("出勤していません")
        bunb="出勤していません"
        return bunb


def culc(date,lastdate):
    session=Session()
    a=emplistcheck()
    ids=list(a.keys())
    text=''
    for aaa in ids:
        total=datetime.timedelta()
        record = session.query(User).filter(
        User.nameid == aaa,
        User.starttime >= date,
        User.finishtime <= lastdate
        ).all()
        for r in record:
            if r.finishtime is None:
                continue
            else:
                workingtime=r.finishtime-r.starttime
                total+=workingtime

        
        namename=a[aaa]+"\n"
        text+=namename
        totall=str(total)
        text+=(totall+"\n")

        hours = total.total_seconds()/3600
        if hours>= 8:
            hours-=1
            kyukei=hours*1140
            print(kyukei)
        elif hours>= 6:
            hours-=0.75
            kyukei=hours*1140
            print(kyukei)
        else:
            money=hours*1140
            text+=(str(money)+"円\n")
        text+="--------------------------------------------\n"
    
    return text
def culc_kojin(nm,date,lastdate):
    session=Session()
    total=datetime.timedelta()
    kyuyomatome=0
    record = session.query(User).filter(
    User.nameid == nm,
    User.starttime >= date,
    User.finishtime <= lastdate
        ).all()
    for r in record:
        print(r.starttime, r.finishtime)
        if r.finishtime is None:
            continue
        else:
            workingtime=r.finishtime-r.starttime
            total+=workingtime

            wktk=workingtime.total_seconds()/3600
            if wktk>=8:
                wktk-=1
                kyuyo=wktk*1140
                kyuyomtome+=kyuyo
            elif wktk>= 6:
                wktk-=0.75
                kyuyo=wktk*1140
                kyuyomatome+=kyuyo
            else:
                kyuyo=wktk*1140
                kyuyomatome+=kyuyo
    kyuyomatome2=str(kyuyomatome)
    kyukk=kyuyomatome2+"円"
    #print(total)
    total2=str(total)
    return total2,kyukk

def yameru(n):
    session=Session()
    employee = session.query(Employee).filter(
        Employee.id == n
    ).first()
    employee.active = False

    session.commit()
def hukki(n):
    session=Session()
    employee = session.query(Employee).filter(
        Employee.id == n
    ).first()
    employee.active = True

    session.commit()
