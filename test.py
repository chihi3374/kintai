import customtkinter
from tkcalendar import Calendar
from quuuuuux import start
from quuuuuux import stop
from sql import emplistcheck
import time
import datetime
from sql import culc_kojin
from sql import culc
from sql import addname
from sql import firelistcheck
from sql import yameru
from sql import hukki
app = customtkinter.CTk()
app.geometry("400x300")
namefrom=emplistcheck()
names = namefrom.values()
a=0
name3=None
numberz=None
timestart=datetime.timedelta()
timestop=datetime.timedelta()

after_id=None
# ======================
# フレーム作成
# ======================
frame1 = customtkinter.CTkFrame(app)
frame2 = customtkinter.CTkFrame(app)
frame3 = customtkinter.CTkFrame(app)
frame4 = customtkinter.CTkFrame(app)
frame5 = customtkinter.CTkFrame(app)
frame6 = customtkinter.CTkFrame(app)
frame7 =  customtkinter.CTkFrame(app)








# ======================
# 画面切り替え関数
# ======================
def show_frame1():
    frame4.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame1.pack(fill="both", expand=True)

def show_frame2():
    frame4.pack_forget()
    frame1.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame2.pack(fill="both", expand=True)
def show_frame3(n):
    global name3
    frame4.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame3.pack(fill="both", expand=True)
    name3=n

def show_frame4():
    frame2.pack_forget()
    frame1.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame4.pack(fill="both", expand=True)
def show_frame5():
    frame2.pack_forget()
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame5.pack(fill="both", expand=True)
def show_frame6():
    frame2.pack_forget()
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame7.pack_forget()
    frame6.pack(fill="both", expand=True)
def show_frame7():
    frame2.pack_forget()
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack(fill="both", expand=True)


def plus():
    global a
    a+=1
    nameshow()
    show_frame2()

def minus():
    global a
    a-=1
    nameshow()
    show_frame2()


def unko():
    global name3
    nameshow()
    show_frame2()
    name3=None


def nameshow():#フレーム２のパーツをおいてく関数
    global a
    for widget in frame2.winfo_children():
        if widget not in (label2, bunlabel,modorubutton):
            widget.destroy()
    namefromx=emplistcheck()
    namesx = namefromx.values()
    for name in namesx:
        button = customtkinter.CTkButton(
            frame2,
            text=name,
            command=lambda n=name: syukkinortaikin(n)
            )
        button.pack(pady=5)
    print(a,"aの値")
    button = customtkinter.CTkButton(frame2, text="全社員",command=kyuuyokeisan)

    flag = False  # 条件（ここ変える）
    if a == 0:
        button.pack(pady=20)

#def new3(n)#フレーム３のパーツをおいてく関数





























# ======================
# フレーム1（最初の画面）メインメニュー
# ======================
label1 = customtkinter.CTkLabel(frame1, text="勤怠管理システムです")
label1.pack(pady=20)

button1 = customtkinter.CTkButton(frame1, text="出勤", command=plus)
button1.pack()


button1 = customtkinter.CTkButton(frame1, text="退勤", command=minus)
button1.pack()


button1 = customtkinter.CTkButton(frame1, text="給与計算", command=unko)
button1.pack()


button1 = customtkinter.CTkButton(frame1, text="従業員追加", command=show_frame5)
button1.pack()

button1 = customtkinter.CTkButton(frame1, text="従業員停止・復帰", command=show_frame6)
button1.pack()







# ======================フレーム３勤怠
cal3 = Calendar(frame3, selectmode='day')
cal3.pack(pady=20)

date_label = customtkinter.CTkLabel(frame3, text="日付がここに出る")
date_label.pack(pady=10)

date_label2 = customtkinter.CTkLabel(frame3, text="日付がここに出る")
date_label2.pack(pady=5)

date_label3 = customtkinter.CTkLabel(frame3, text="")
date_label3.pack(pady=0)





def get_date():
    global name3
    global numberz
    global timestart
    date = cal3.get_date()
    m, d, y = date.split("/")  # 分解

    new_date = f"{y}/{m}/{d}" 
    yy=int(y)
    mm=int(m)
    dd=int(d)
    datetimestyle= datetime.datetime(2000+yy, mm, dd, 0, 0, 0)
    date_label.configure(text="開始日："+new_date)  # ←ここがポイント

    reverse = {v: k for k, v in namefrom.items()}
    number=reverse[name3]#######従業員id
    numberz=int(number)
    timestart=datetimestyle










def get_date2():


    global name3
    global numberz
    global timestop
    date = cal3.get_date()
    m, d, y = date.split("/")  # 分解

    new_date = f"{y}/{m}/{d}" 
    yy=int(y)
    mm=int(m)
    dd=int(d)

    datetimestyle= datetime.datetime(2000+yy, mm, dd, 23, 59, 59)
    date_label2.configure(text="締め日："+new_date)  

    reverse = {v: k for k, v in namefrom.items()}
    number=reverse[name3]#######従業員id
    numberz=int(number)
    timestop=datetimestyle
    print(timestop)

def modorouyo():
    global name3
    global numberz
    global timestop
    global timestart
    name3=None
    numberz=None
    timestop=None
    timestart=None################################################################
    date_label.configure(text="日付がここに出る")
    date_label2.configure(text="日付がここに出る")
    date_label3.configure(text="")
    date4_label.configure(text="日付がここに出る")
    date4_label2.configure(text="日付がここに出る")
    show_frame2()







def culcexpo():
    r=culc_kojin(numberz,timestart,timestop)
    print(r)############################################
    rr=str(r)
    date_label3.configure(text="勤務時間/給与："+rr)



button = customtkinter.CTkButton(frame3, text="開始日", command=get_date)
button.pack()
button2 =customtkinter.CTkButton(frame3, text="締め日", command=get_date2)
button2.pack()

button4 =customtkinter.CTkButton(frame3, text="計算", command=culcexpo)
button4.pack()

button3 =customtkinter.CTkButton(frame3, text="戻る", command=modorouyo)
button3.pack()








# フレーム2（次の画面）名前セレクト
# ======================
def taikin(n):#退勤処理
    global after_id
    reverse = {v: k for k, v in namefrom.items()}
    number=reverse[n]
    bun=stop(number)
    bunlabel.configure(text=bun)
    if after_id is not None:
        try:
            app.after_cancel(after_id)
        except:
            pass
    after_id=app.after(2000, lambda: bunlabel.configure(text=""))
def newgamen(n):#個人給与計算
    print(n, "計算")
    show_frame3(n)





label2 = customtkinter.CTkLabel(frame2, text="名前を選択してください")
label2.pack(pady=20)
bunlabel = customtkinter.CTkLabel(frame2, text=" ")
bunlabel.pack(pady=15)

def modoru():
    global a
    a=a*0
    show_frame1()
    print(a)


modorubutton = customtkinter.CTkButton(
frame2,
text="戻る",
command=modoru
)
modorubutton.pack(pady=15)




def kyuuyokeisan():
    print("全員分計算します")
    show_frame4()

def syukkinortaikin(n):########## aの正負もしくは０でnameshowのボタンのコマンドを変更する関数　出勤退勤　給与計算の名簿選択
    global a
    if a  ==1:
        syukkin(n)
    elif a ==-1:
        taikin(n)
    else:
        newgamen(n)




def syukkin(n):#n=名前　出勤処理
    global after_id
    reverse = {v: k for k, v in namefrom.items()}
    number=reverse[n]
    bun=start(number)
    bunlabel.configure(text=bun)
    print(n, "出勤")
    if after_id is not None:
        try:
            app.after_cancel(after_id)
        except:
            pass
    after_id=app.after(2000, lambda: bunlabel.configure(text=""))
    

###########################################################################全社員計算＃＃＃＃＃＃＃＃＃＃＃＃＃＃
# ======================フレーム4勤怠
cal = Calendar(frame4, selectmode='day')
cal.pack(pady=20)

date4_label = customtkinter.CTkLabel(frame4, text="日付がここに出る")
date4_label.pack(pady=10)

date4_label2 = customtkinter.CTkLabel(frame4, text="日付がここに出る")
date4_label2.pack(pady=5)

date4_label3 = customtkinter.CTkLabel(frame4, text="")
date4_label3.pack(pady=0)




def get_date4():
    global timestart
    date = cal.get_date()
    m, d, y = date.split("/")  # 分解

    new_date = f"{y}/{m}/{d}" 
    yy=int(y)
    mm=int(m)
    dd=int(d)
    datetimestyle= datetime.datetime(2000+yy, mm, dd, 0, 0, 0)
    date4_label.configure(text="開始日："+new_date)  # ←ここがポイント

    reverse = {v: k for k, v in namefrom.items()}

    timestart=datetimestyle


def get_date42():

    global timestop
    date = cal.get_date()
    m, d, y = date.split("/")  # 分解

    new_date = f"{y}/{m}/{d}" 
    yy=int(y)
    mm=int(m)
    dd=int(d)

    datetimestyle= datetime.datetime(2000+yy, mm, dd, 23, 59, 59)
    date4_label2.configure(text="締め日："+new_date)  

    reverse = {v: k for k, v in namefrom.items()}
    timestop=datetimestyle
    print(timestop)




def allculc():
    a=culc(timestart,timestop)
    print(a)

    new_win = customtkinter.CTkToplevel()
    new_win.title("時間・給与：全社員")
    new_win.geometry("300x200")
    
    # 新規ウィンドウにラベルを配置
    label = customtkinter.CTkLabel(new_win, text=a,text_color="red")
    label.pack(pady=20)





####################やらなきゃんこと☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
                    #従業員　追加　停止　停止解除コマンド
                    #コンパイル
















button = customtkinter.CTkButton(frame4, text="開始日", command=get_date4)
button.pack()
button2 =customtkinter.CTkButton(frame4, text="締め日", command=get_date42)
button2.pack()

button4 =customtkinter.CTkButton(frame4, text="計算", command=allculc)
button4.pack()

button3 =customtkinter.CTkButton(frame4, text="戻る", command=modorouyo)
button3.pack()

#######################################################################################frame5 従業員追加
date5_label = customtkinter.CTkLabel(frame5, text="従業員追加")
date5_label.pack(pady=10)

date5_label2 = customtkinter.CTkLabel(frame3, text="")
date5_label2.pack(pady=15)

def show_input():
    # 入力された文字を取得
    user_input = entry.get()
    print(f"入力された文字: {user_input}")
    addname(user_input)
    # ラベルに反映
    date5_label2.configure(text=f"{user_input}を追加しました")

def modoritai():
    date5_label2.configure(text="")
    entry.delete(0, "end")
    show_frame1()




# 1. 入力欄（CTkEntry）の作成
entry = customtkinter.CTkEntry(frame5, placeholder_text="ここに文字を入力してください", width=250)
entry.pack(pady=20)

# 2. 決定ボタン
button = customtkinter.CTkButton(frame5, text="追加", command=show_input)
button.pack(pady=10)

button = customtkinter.CTkButton(frame5, text="戻る", command=modoritai)
button.pack(pady=10)


######################################################################################################################6666666666666666666666666



button = customtkinter.CTkButton(frame6, text="復帰", command=lambda:destroymake("0"))
button.pack(pady=10)

buttonz = customtkinter.CTkButton(frame6, text="休職", command=lambda:destroymake("1"))
buttonz.pack(pady=10)

kaeru = customtkinter.CTkButton(frame6, text="戻る", command=show_frame1)
kaeru.pack(pady=10)
##############################################################################################7777777777777777777777777777777777777777777777777777
def kyusyoku(n):
    print("a")
    yameru(n)
def fukki(n):
    print("a")
    hukki(n)





def destroymake(m):
    for widget in frame7.winfo_children():
        if widget != modoru77:
            widget.destroy()
    if m=="0":
        firelist=firelistcheck()
        if firelist==None:
            print("なにもいない")
        else:
            namesfire = firelist.values()
            reverse = {v: k for k, v in firelist.items()}
            label777 = customtkinter.CTkLabel(frame7, text="復帰する従業員をクリックしてください")
            label777.pack(pady=10)

            for name in namesfire:

                num=reverse[name]

                button = customtkinter.CTkButton(
                    frame7,
                    text=name,
                    command=lambda num=num: fukki(num)
                    )
                button.pack(pady=5)
            show_frame7()
    elif m=="1":
        emplist=emplistcheck()
        namesemp = emplist.values()
        reverseemp = {v: k for k, v in emplist.items()}
        label777 = customtkinter.CTkLabel(frame7, text="休職・出勤停止する従業員をクリックしてください")
        label777.pack(pady=10)

        for nameemp in namesemp:
            numemp=reverseemp[nameemp]
            button = customtkinter.CTkButton(
                frame7,
                text=nameemp,
                command=lambda numemp=numemp: kyusyoku(numemp)
                )
            button.pack(pady=5)
        show_frame7()
        

modoru77 = customtkinter.CTkButton(frame7, text="戻る", command=show_frame6)
modoru77.pack(pady=10)














##########################給与計算フラグで出退勤時にはない　すべてボタンを追加　global aで判断　出退勤フラグのときは出ないように
nameshow()
# 最初に表示するページ
show_frame1()

app.mainloop()