from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import threading
import datetime
import pandas as pd
import video
import audio
import random
from tkinter import messagebox
import pyautogui as pag
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"


global interval

interval = 120
relax_interval = 120

scr_w, scr_h = pag.size()
print("画面サイズの幅：", scr_w)
print("画面サイズの高さ：", scr_h)

video = video.Video()
audio = audio.Audio()

task_count=5

def click_close():
    if messagebox.askokcancel("確認", "本当に閉じていいですか？"):
        close()
        return 0

def close():
    root.destroy()

def QUESTION():

    one = random.randint(10, 90)
    two = random.randint(10, 90)

    hugo = ["×"]
    ans = [one * two]

    # 問題をランダムに生成
    hugo = hugo[0]
    ans = ans[0]
    radio_button_list = [ans, ans - 10, ans + 10, ans + two]
    random.shuffle(radio_button_list)  # 配列の中をシャッフル
    question = "{} {} {} = ".format(one, hugo, two)

    print("hugo", hugo)
    print("ans", ans)

    return ans, question, radio_button_list

def question_language(i):

    if count == 1:
        if i==0:
            genre="似た意味の単語"
            ans = "忍耐"
            question = "我慢"
            radio_button_list = ["忍耐", "精神", "自慢"]
        elif i==1:
            genre="反対の意味の単語"
            ans = "減る"
            question = "増える"
            radio_button_list = ["減る", "取る", "引く"]
        elif i==2:
            genre="似た意味の単語"
            ans = "ふるさと"
            question = "田舎"
            radio_button_list = ["農家", "都会", "ふるさと"]
        elif i==3:
            genre="反対の意味の単語"
            ans = "下がる"
            question = "上がる"
            radio_button_list = ["下がる", "止まる", "登る"]
        elif i==4:
            genre="似た意味の単語"
            ans = "いただく"
            question = "もらう"
            radio_button_list = ["あげる", "いただく", "買う"]
        elif i==5:
            genre="反対の意味の単語"
            ans = "座る"
            question = "立つ"
            radio_button_list = ["降りる", "座る", "寝る"]
        elif i==6:
            genre="似た意味の単語"
            ans = "でかける"
            question = "行く"
            radio_button_list = ["話す", "帰る", "でかける"]
        elif i==7:
            genre="反対の意味の単語"
            ans = "寝る"
            question = "起きる"
            radio_button_list = ["座る", "冷める", "寝る"]
        elif i==8:
            genre="似た意味の単語"
            ans = "必修"
            question = "必要"
            radio_button_list = ["用心", "必修", "用意"]
        elif i==9:
            genre="反対の意味の単語"
            ans = "配る"
            question = "集める"
            radio_button_list = ["配る", "もらう", "渡す"]
        elif i==10:
            genre="似た意味の単語"
            ans = "昔"
            question = "過去"
            radio_button_list = ["昔", "現在", "未来"]
        elif i==11:
            genre="反対の意味の単語"
            ans = "閉じる"
            question = "開く"
            radio_button_list = ["押す", "しまう", "閉じる"]
        elif i==12:
            genre="似た意味の単語"
            ans = "くるむ"
            question = "包む"
            radio_button_list = ["しめる", "くるむ", "たたく"]
        elif i==13:
            genre="反対の意味の単語"
            ans = "降りる"
            question = "乗る"
            radio_button_list = ["下がる", "座る", "降りる"]
        elif i==14:
            genre="似た意味の単語"
            ans = "農民"
            question = "百姓"
            radio_button_list = ["穀物", "百合", "農民"]
        elif i==15:
            genre="反対の意味の単語"
            ans = "拾う"
            question = "捨てる"
            radio_button_list = ["拾う", "集める", "ゆずる"]
        elif i==16:
            genre="似た意味の単語"
            ans = "かせぐ"
            question = "もうける"
            radio_button_list = ["かせぐ", "経費", "利益"]
        elif i==17:
            genre="反対の意味の単語"
            ans = "吐く"
            question = "吸う"
            radio_button_list = ["戻す", "吐く", "押す"]
        elif i==18:
            genre="似た意味の単語"
            ans = "伝達する"
            question = "送る"
            radio_button_list = ["かける", "伝達する", "はしる"]
        elif i==19:
            genre="反対の意味の単語"
            ans = "逃げる"
            question = "追う"
            radio_button_list = ["攻める", "止まる", "逃げる"]
        elif i==20:
            genre="似た意味の単語"
            ans = "生涯"
            question = "一生"
            radio_button_list = ["半生", "生涯", "一期"]
        elif i==21:
            genre="反対の意味の単語"
            ans = "貸す"
            question = "借りる"
            radio_button_list = ["もらう", "貸す", "渡す"]
        elif i==22:
            genre="似た意味の単語"
            ans = "先生"
            question = "教員"
            radio_button_list = ["先生", "生徒", "リーダー"]
        elif i==23:
            genre="反対の意味の単語"
            ans = "入る"
            question = "出る"
            radio_button_list = ["登る", "入る", "しまう"]

    if count == 3:
        if i==0:
            genre="似た意味の単語"
            ans = "経験"
            question = "体験"
            radio_button_list = ["試験", "実験", "経験"]
        elif i==1:
            genre="反対の意味の単語"
            ans = "終わる"
            question = "始める"
            radio_button_list = ["続ける", "決める", "終わる"]
        elif i==2:
            genre="似た意味の単語"
            ans = "用意"
            question = "準備"
            radio_button_list = ["用意", "引越", "開始"]
        elif i==3:
            genre="反対の意味の単語"
            ans = "脱ぐ"
            question = "着る"
            radio_button_list = ["履く", "直る", "脱ぐ"]
        elif i==4:
            genre="似た意味の単語"
            ans = "暖かい"
            question = "温かい"
            radio_button_list = ["湯気", "あつい", "暖かい"]
        elif i==5:
            genre="反対の意味の単語"
            ans = "売る"
            question = "買う"
            radio_button_list = ["渡す", "売る", "払う"]
        elif i==6:
            genre="似た意味の単語"
            ans = "悪党"
            question = "悪人"
            radio_button_list = ["悪党", "悪相", "悪僧"]
        elif i==7:
            genre="反対の意味の単語"
            ans = "やわらかい"
            question = "固い"
            radio_button_list = ["丸い", "薄い", "やわらかい"]
        elif i==8:
            genre="似た意味の単語"
            ans = "よごれた"
            question = "きたない"
            radio_button_list = ["下品な", "らんぼうな", "よごれた"]
        elif i==9:
            genre="反対の意味の単語"
            ans = "敵"
            question = "味方"
            radio_button_list = ["他人", "敵", "友人"]
        elif i==10:
            genre="似た意味の単語"
            ans = "干す"
            question = "乾かす"
            radio_button_list = ["仕上げる", "干す", "あげる"]
        elif i==11:
            genre="反対の意味の単語"
            ans = "引く"
            question = "押す"
            radio_button_list = ["たたく", "引く", "回す"]
        elif i==12:
            genre="似た意味の単語"
            ans = "げんなり"
            question = "うんざり"
            radio_button_list = ["うるさい", "げんなり", "辛辣"]
        elif i==13:
            genre="反対の意味の単語"
            ans = "守る"
            question = "攻める"
            radio_button_list = ["弱まる", "押す", "守る"]
        elif i==14:
            genre="似た意味の単語"
            ans = "あつまり"
            question = "よりあい"
            radio_button_list = ["相談", "もつ", "あつまり"]
        elif i==15:
            genre="反対の意味の単語"
            ans = "出力"
            question = "入力"
            radio_button_list = ["出力", "挿入", "開示"]
        elif i==16:
            genre="似た意味の単語"
            ans = "しゃべる"
            question = "話す"
            radio_button_list = ["笑う", "歌う", "しゃべる"]
        elif i==17:
            genre="反対の意味の単語"
            ans = "遅い"
            question = "早い"
            radio_button_list = ["遅い", "長い", "低い"]
        elif i==18:
            genre="似た意味の単語"
            ans = "見失う"
            question = "はぐれる"
            radio_button_list = ["見失う", "歩く", "みる"]
        elif i==19:
            genre="反対の意味の単語"
            ans = "入れる"
            question = "出す"
            radio_button_list = ["閉じる", "入れる", "押す"]
        elif i==20:
            genre="似た意味の単語"
            ans = "さわる"
            question = "ふれる"
            radio_button_list = ["たたく", "つまむ", "さわる"]
        elif i==21:
            genre="反対の意味の単語"
            ans = "寒い"
            question = "暑い"
            radio_button_list = ["上がる", "暖かい", "寒い"]
        elif i==22:
            genre="似た意味の単語"
            ans = "おくびょう"
            question = "こわい"
            radio_button_list = ["おくびょう", "強い", "おそろしい"]
        elif i==23:
            genre="反対の意味の単語"
            ans = "薄い"
            question = "濃い"
            radio_button_list = ["明るい", "薄い", "弱い"]


    return ans, question, radio_button_list, genre

####切り替えボタン####
def change():
    global canvas2
    canvas2 = tk.Canvas(root, highlightthickness=0)
    canvas2.pack(
        fill=tk.BOTH, expand=True
    )  # configure canvas to occupy the whole main window
    # 各種ウィジェットの作成
    label1_frame_app = tk.Label(canvas2, text="準備ができたら課題に進んでください", font=("", 40))
    button_change_frame_app = tk.Button(
        canvas2, text="進む", font=("", 40), bg="grey", command=lambda: task_select(),relief="solid"
    )
    # logに書き込み
    log.logging(
        situation="準備ができたら課題に進んでください",
        action="-",
        user_input="-",
        correct="-",
        judge="-",
        evaluation="-",
        eye_ans="-",
        ans_position="-",
        eye_correct="-",
        choice_1="-",
        choice_2="-",
        choice_3="-",
        choice_4="-",
    )
    # 各種ウィジェットの設置
    label1_frame_app.pack(anchor="center", expand=1)
    button_change_frame_app.pack(anchor="center", expand=1)


####relax動画####
def timecount(canvas, video, audio):
    second = 0
    flg = True
    # time_label = tk.Label(canvas, text="", font=("",20))
    # time_label.pack(anchor='nw',expand=0)
    while flg:
        second += 1
        time.sleep(1)  # convert second to hour, minute and seconds
        elapsed_minute = (second % 3600) // 60
        elapsed_second = second % 3600 % 60
        # print as 00:00:00
        print(str(elapsed_minute).zfill(2) + ":" + str(elapsed_second).zfill(2))
        # time_label.configure(text=f"経過時間：{str(elapsed_minute).zfill(2)}:{str(elapsed_second).zfill(2)}")

        # print(interval)
        if second == relax_interval:
            # logに書き込み
            log.logging(
                situation="リラックスモード終了",
                action="-",
                user_input="-",
                correct="-",
                judge="-",
                evaluation="-",
                eye_ans="-",
                ans_position="-",
                eye_correct="-",
                choice_1="-",
                choice_2="-",
                choice_3="-",
                choice_4="-",
            )

            video.stop()
            audio.stop()
            canvas.destroy()
            change()
            flg = False
            return 0


def movie(canvas1,v1):
    print("集中度:%s" % v1.get())

    # logに書き込み
    log.logging(
        situation="集中度の自己評価",
        action="okボタン押した",
        user_input="-",
        correct="-",
        judge="-",
        evaluation=str(v1.get()),
        eye_ans="-",
        ans_position="-",
        eye_correct="-",
        choice_1="-",
        choice_2="-",
        choice_3="-",
        choice_4="-",
    )


    canvas1.destroy()
    canvas = tk.Canvas(root, highlightthickness=0)
    canvas.pack(
        fill=tk.BOTH, expand=True
    )  # configure canvas to occupy the whole main window
    label = tk.Label(canvas, text="2分間休憩時間です", font=("", 40))
    label.pack(anchor="center", expand=1)

    # logに書き込み
    log.logging(
        situation="リラックスモードに移行(2分休憩スライド)",
        action="-",
        user_input="-",
        correct="-",
        judge="-",
        evaluation="-",
        eye_ans="-",
        ans_position="-",
        eye_correct="-",
        choice_1="-",
        choice_2="-",
        choice_3="-",
        choice_4="-",
    )

    # sleep 前のエポック秒(UNIX時間)を取得
    startSec = time.time()
    canvas.frame = tk.Label(canvas)
    canvas.frame.pack(side=tk.BOTTOM)
    video.openfile("./relax.mp4", canvas.frame)
    audio.openfile("./relax.wav")
    Q=[label,canvas]
    root.after(
        3000,
        image_de,
        Q
    )

def image_de(Q):
    label=Q[0]
    canvas=Q[1]
    label.pack_forget()
    # 経過時間スレッドの開始
    thread = threading.Thread(
        name="thread", target=timecount, args=[canvas, video, audio], daemon=True
    )
    thread.start()

    audio.play()
    video.play()

    # logに書き込み
    log.logging(
        situation="リラックスモード(動画開始)",
        action="-",
        user_input="-",
        correct="-",
        judge="-",
        evaluation="-",
        eye_ans="-",
        ans_position="-",
        eye_correct="-",
        choice_1="-",
        choice_2="-",
        choice_3="-",
        choice_4="-",
    )

def end(canvas):
    label = tk.Label(canvas, text="課題は終了です。", font=("", 40))
    label1 = tk.Label(canvas, text="お疲れ様でした。", font=("", 40))
    label.pack(anchor="center", expand=1)
    label1.pack(anchor="center", expand=1)

    root.after(
        3000,
        close
    )

####課題選択####
def task_select():
    canvas2.destroy()
    canvas1 = tk.Canvas(root, highlightthickness=0)  # ,bg = "cyan")
    canvas1.pack(
        fill=tk.BOTH, expand=True
    )  # configure canvas to occupy the whole main window
    print("count:" + str(count))

    # logに書き込み
    log.logging(
        situation="準備ができたら課題に進んでください",
        action="進むボタンを押した",
        user_input="-",
        correct="-",
        judge="-",
        evaluation="-",
        eye_ans="-",
        ans_position="-",
        eye_correct="-",
        choice_1="-",
        choice_2="-",
        choice_3="-",
        choice_4="-",
    )

    if count == task_count:
        end(canvas1)
    elif count % 2 == 0:
        eye_task(master=canvas1)
    else:
        #Application(master=canvas1)
        Language(master=canvas1)
    # print(App)

####アンケート評価####
def questionnaire():
    canvas = tk.Canvas(root, highlightthickness=0)
    canvas.pack(
        fill=tk.BOTH, expand=True
    )  # configure canvas to occupy the whole main window
    """# Frame
    frame1 = ttk.Frame(root, padding=10)"""
    # Style - Theme
    ttk.Style().configure('MyWidget.TRadiobutton' ,font=(None,30))#, relief="flat",overrelief="raised")
    ttk.Style().map('MyWidget.TRadiobutton',
                    foreground=[ ('active', 'blue')],
                    background=[ ('active', 'white')]
                    )
    #ttk.Style().theme_use("alt")
    label = tk.Label(canvas, text="課題を通して自分の集中度を評価してください", font=("", 30))
    #whi = tk.Label(canvas, text="", font=("", 30))

    # Radiobutton 1
    v1 = StringVar()
    rb1 = ttk.Radiobutton(
        canvas,
        text="1.集中していた",
        value='1',
        style='MyWidget.TRadiobutton',
        variable=v1, command =lambda: change_state(button1))

    # Radiobutton 2
    rb2 = ttk.Radiobutton(
        canvas,
        text='2.少し集中していた',
        value='2',
        style='MyWidget.TRadiobutton',
        variable=v1, command = lambda: change_state(button1))

    # Radiobutton 2
    rb3 = ttk.Radiobutton(
        canvas,
        text='3.どちらでもない',
        value='3',
        style='MyWidget.TRadiobutton',
        variable=v1, command = lambda: change_state(button1))

    # Radiobutton 2
    rb4 = ttk.Radiobutton(
        canvas,
        text='4.少し集中できなかった',
        value='4',
        style='MyWidget.TRadiobutton',
        variable=v1, command = lambda: change_state(button1))

    # Radiobutton 2
    rb5 = ttk.Radiobutton(
        canvas,
        text='5.全く集中できなかった',
        value='5',
        style='MyWidget.TRadiobutton',
        variable=v1, command = lambda: change_state(button1))

    # Button
    button1 = tk.Button(
        canvas,
        text='OK',
        font=("", 30),
        command=lambda: movie(canvas,v1),
        state=tk.DISABLED,relief="solid",
        bg="grey")

    label.pack(anchor="center",expand=1)
    rb1.pack(anchor="center",pady=20)
    rb2.pack(anchor="center",pady=20)
    rb3.pack(anchor="center",pady=20)
    rb4.pack(anchor="center",pady=20)
    rb5.pack(anchor="center",pady=20)
    button1.pack(anchor="center", expand=1)

    # logに書き込み
    log.logging(
        situation="集中度の自己評価アンケートの表示",
        action="-",
        user_input="-",
        correct="-",
        judge="-",
        evaluation="-",
        eye_ans="-",
        ans_position="-",
        eye_correct="-",
        choice_1="-",
        choice_2="-",
        choice_3="-",
        choice_4="-",
    )


def change_state(button1):
    if button1["state"] == tk.DISABLED:
        button1["state"] = tk.NORMAL

####視線課題####
class eye_task(tk.Frame):
    def __init__(self, master):
        # logに書き込み
        log.logging(
            situation="視線課題の説明",
            action="-",
            user_input="-",
            correct="-",
            judge="-",
            evaluation="-",
            eye_ans="-",
            ans_position="-",
            eye_correct="-",
            choice_1="-",
            choice_2="-",
            choice_3="-",
            choice_4="-",
        )

        super().__init__(master)
        # self.pack()
        self.column_data = (0, 0, 1, 1)
        self.row_data = (0, 1, 0, 1)
        # 各種ウィジェットの作成
        self.label1_frame_app = tk.Label(self.master, text="〇", font=("", 100),fg="red")
        self.label2_frame_app = tk.Label(self.master, text="を選択・クリックしてください", font=("", 40))
        self.button_change_frame_app = tk.Button(
            self.master, text="課題に進む", font=("", 40), bg="grey", command=lambda: self.rocate(),relief="solid"
        )
        # 各種ウィジェットの設置
        self.label1_frame_app.pack(anchor="center", expand=1)
        self.label2_frame_app.pack(anchor="center", expand=1)
        self.button_change_frame_app.pack(anchor="center", expand=1)


    def rocate(self):
        # logに書き込み
        log.logging(
            situation="視線課題の説明",
            action="進むボタンを押した",
            user_input="-",
            correct="-",
            judge="-",
            evaluation="-",
            eye_ans="-",
            ans_position="-",
            eye_correct="-",
            choice_1="-",
            choice_2="-",
            choice_3="-",
            choice_4="-",
        )
        self.label1_frame_app.pack_forget()
        self.label2_frame_app.pack_forget()
        self.button_change_frame_app.pack_forget()

        self.text = self.random_symbol()
        self.flg = True

        self.symbol = []
        self.button = []
        # logに書き込み
        log.logging(
            situation="視線課題の開始",
            action="進むボタンを押した",
            user_input="-",
            correct="-",
            judge="-",
            evaluation="-",
            eye_ans="-",
            ans_position="-",
            eye_correct="-",
            choice_1="-",
            choice_2="-",
            choice_3="-",
            choice_4="-",
        )
        #print(self.text)
        for i in range(4):
            self.symbol.append(tk.StringVar())
            self.symbol[i].set(self.text[i][0])
            # print(self.symbol[i])
            self.button.append(
                tk.Button(
                    self.master,
                    textvariable=self.symbol[i],
                    fg=self.text[i][1],
                    font=("", 100),
                )
            )
            self.button[i].grid(
                column=self.column_data[i],
                row=self.row_data[i],
                padx=30,
                pady=30,
                sticky="nsew",
            )
            # ボタンクリック時のイベント設定
            self.button[i].bind("<ButtonPress>",  (lambda e, num=i: self.button_func(e, num)))

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)

        # 経過時間スレッドの開始
        self.t = threading.Thread(target=self.timer, daemon=True)
        self.t.start()

    def random_symbol(self):  # 問題作成
        self.text = [["〇", "red"]]
        self.label = ["〇", "△", "□", "×"]
        self.color = ["red"]#, "green", "blue", "yellow"]

        for i in range(3):
            self.a = random.choice(self.label)
            self.b = random.choice(self.color)
            while self.a == "〇" and self.b == "red":
                self.a = random.choice(self.label)
                self.b = random.choice(self.color)
            self.text.append([self.a, self.b])
        random.shuffle(self.text)
        self.pos = self.text
        return self.text

    def button_func(self, event,num):
        if num == 0:
            position = "第2象限"
        elif num == 1:
            position = "第3象限"
        elif num == 2:
            position = "第1象限"
        elif num == 3:
            position = "第4象限"
        # logに書き込み
        log.logging(
            situation="集中",
            action="userがボタン入力",
            user_input="-",
            correct="-",
            judge="-",
            evaluation="-",
            eye_ans=str(event.widget.cget("text")),
            ans_position=str(position),
            eye_correct="〇",
            choice_1=str(self.pos[2][0]),
            choice_2=str(self.pos[0][0]),
            choice_3=str(self.pos[1][0]),
            choice_4=str(self.pos[3][0]),

        )
        # event.widget.config(fg="red")
        print(position)
        print("形:" + event.widget.cget("text") + "　色:" + event.widget.cget("fg"))
        for i in range(4):
            self.button[i].grid_forget()
        self.master.create_text(
            scr_w / 2, scr_h / 2, text="●", font=("", 40), tag="line"
        )

        # 1000ms後にchange_label_textを実行
        root.after(
            1000,
            self.change_label_text,
        )

    def timer(self):
        self.second = 0
        self.flg = True
        # print(self.second)
        while self.flg:
            # print(self.second)
            self.second += 1
            time.sleep(1)

            # 2分経ったら
            if self.second == interval:
                # logに書き込み
                log.logging(
                    situation="視線課題の終了",
                    action="-",
                    user_input="-",
                    correct="-",
                    judge="-",
                    evaluation="-",
                    eye_ans="-",
                    ans_position="-",
                    eye_correct="-",
                    choice_1="-",
                    choice_2="-",
                    choice_3="-",
                    choice_4="-",
                )
                self.second = 0
                self.destroy()
                self.master.destroy()
                global count
                count += 1
                self.flg = False
                print("----------------------")
                questionnaire()

                return 0

    def change_label_text(self):
        self.text = self.random_symbol()
        print(self.flg)
        if self.flg == True:
            self.master.delete("line")
            for i in range(4):
                self.symbol[i].set(self.text[i][0])
                self.button[i]["fg"] = self.text[i][1]
                self.button[i].grid(
                    column=self.column_data[i],
                    row=self.row_data[i],
                    padx=30,
                    pady=30,
                    sticky="nsew",
                )

"""
####計算課題####
class Application(tk.Frame):
    def __init__(self, master):
        # logに書き込み
        log.logging(
            situation="計算課題の説明",
            action="-",
            user_input="-",
            correct="-",
            judge="-",
            evaluation="-",
            eye_ans="-",
            ans_position="-",
            eye_correct="-",
            choice_1="-",
            choice_2="-",
            choice_3="-",
            choice_4="-",
        )

        super().__init__(master)
        self.pack()

        # 問題数インデックス
        self.index = 0

        # 正解数カウント用
        self.correct_cnt = 0


        # self.pack()
        self.column_data = (0, 0, 1, 1)
        self.row_data = (0, 1, 0, 1)
        # 各種ウィジェットの作成
        self.label1_frame_app = tk.Label(self.master, text="2桁の ＋,－,× を行います", font=("", 40))#,fg="red")
        self.label2_frame_app = tk.Label(self.master, text="4択のうち正しい答えを選択し決定してください", font=("", 40))
        self.button_change_frame_app = tk.Button(
            self.master, text="課題に進む", font=("", 40), bg="grey", command=lambda: self.rocate(),relief="solid"
        )
        # 各種ウィジェットの設置
        self.label1_frame_app.pack(anchor="center", expand=1)
        self.label2_frame_app.pack(anchor="center", expand=1)
        self.button_change_frame_app.pack(anchor="center", expand=1)


    def rocate(self):
        # logに書き込み
        log.logging(
            situation="計算課題の説明",
            action="進むボタンを押した",
            user_input="-",
            correct="-",
            judge="-",
            evaluation="-",
            eye_ans="-",
            ans_position="-",
            eye_correct="-",
            choice_1="-",
            choice_2="-",
            choice_3="-",
            choice_4="-",
        )
        self.label1_frame_app.pack_forget()
        self.label2_frame_app.pack_forget()
        self.button_change_frame_app.pack_forget()
        self.create_widgets()

        # 経過時間スレッドの開始
        self.t = threading.Thread(target=self.timer, daemon=True)
        self.t.start()

        # Tkインスタンスに対してキーイベント処理を実装
        # self.master.bind("<KeyPress>", self.type_event)

    # ウィジェットの生成と配置
    def create_widgets(self):
        # logに書き込み
        log.logging(
            situation="計算課題の開始",
            action="-",
            user_input="-",
            correct="-",
            judge="-",
            evaluation="-",
            eye_ans="-",
            ans_position="-",
            eye_correct="-",
            choice_1="-",
            choice_2="-",
            choice_3="-",
            choice_4="-",
        )
        self.ans_label2 = tk.Label(self, text="", width=10, anchor="w", font=("", 40))
        self.ans_label2.grid(row=0, column=0)
        self.q_label = tk.Label(self, text="お題：", font=("", 40))
        self.q_label.grid(row=1, column=0)

        # 問題作成
        self.ans, q, radio_button_list = QUESTION()
        self.q_label2 = tk.Label(self, text=q, width=20, anchor="w", font=("", 40))
        self.q_label2.grid(row=1, column=1)
        self.ans_label = tk.Label(self, text="解答：", font=("", 40))
        self.ans_label.grid(row=2, column=0)
        self.answer = tk.Label(self, text="", width=20, anchor="w", font=("", 40))
        self.answer.grid(row=2, column=1)

        self.result_label = tk.Label(self, text="", font=("", 40))
        self.result_label.grid(row=3, column=0, columnspan=2)

        # ウィジェットの作成
        self.radio_value = tk.IntVar()  # ラジオボタンの初期値を0にする

        # ラジオボタンの作成
        self.radio0 = tk.Radiobutton(
            self.master,
            text=str(radio_button_list[0]),  # ラジオボタンの表示名
            command=self.radio_click,  # クリックされたときに呼ばれるメソッド
            variable=self.radio_value,  # 選択の状態を設定する
            value=str(radio_button_list[0]),  # ラジオボタンに割り付ける値の設定
            indicator=0,
            background="light blue",
            font=("", 20),
            width=20,
            height=3,
        )

        self.radio1 = tk.Radiobutton(
            self.master,
            text=str(radio_button_list[1]),  # ラジオボタンの表示名
            command=self.radio_click,  # クリックされたときに呼ばれるメソッド
            variable=self.radio_value,  # 選択の状態を設定する
            value=str(radio_button_list[1]),  # ラジオボタンに割り付ける値の設定
            indicator=0,
            background="light blue",
            font=("", 20),
            width=20,
            height=3,
        )

        self.radio2 = tk.Radiobutton(
            self.master,
            text=str(radio_button_list[2]),  # ラジオボタンの表示名
            command=self.radio_click,  # クリックされたときに呼ばれるメソッド
            variable=self.radio_value,  # 選択の状態を設定する
            value=str(radio_button_list[2]),  # ラジオボタンに割り付ける値の設定
            indicator=0,
            background="light blue",
            font=("", 20),
            width=20,
            height=3,
        )

        self.radio3 = tk.Radiobutton(
            self.master,
            text=str(radio_button_list[3]),  # ラジオボタンの表示名
            command=self.radio_click,  # クリックされたときに呼ばれるメソッド
            variable=self.radio_value,  # 選択の状態を設定する
            value=str(radio_button_list[3]),  # ラジオボタンに割り付ける値の設定
            indicator=0,
            background="light blue",
            font=("", 20),
            width=20,
            height=3,
        )

        # ボタンの作成
        self.button = tk.Button(
            self.master,
            text="OK",  # ボタンの表示名
            command=self.button_click,  # クリックされたときに呼ばれるメソッド
            relief="solid",
            state=tk.DISABLED,
            width=20,
            height=3,
            bg="grey",
        )

        # ボタンクリックに対してキーイベント処理を実装
        # self.button.bind("<ButtonPress>", self.type_event)

        # ウィジェットの設置
        self.radio0.pack()
        self.radio1.pack()
        self.radio2.pack()
        self.radio3.pack()
        self.button.pack(expand=1)

        # # 時間計測用のラベル
        self.time_label = tk.Label(self, text="", font=("", 20))
        self.time_label.grid(row=4, column=0, columnspan=2)
        self.result_label = tk.Label(self, text="", font=("", 20))
        self.result_label.grid(row=5, column=0, columnspan=2)

        self.flg2 = True

    def radio_click(self):
        # ラジオボタンの値を取得
        value = self.radio_value.get()
        print(f"ラジオボタンの値は {value} です")
        self.answer.configure(text=value)
        if self.button["state"] == tk.DISABLED:
            self.button["state"] = tk.NORMAL
            self.button["bg"] = "white"

        # "OK"のボタンを押したかどうか
        self.next = False

    # def button_click(self):
    #     # 問題を次に移動させるフラグを立てる
    #     value = self.radio_value.get()
    #     self.ans_label2 = value
    #     self.next = True

    # キー入力時のイベント処理
    def button_click(self):
        global log
        value = self.radio_value.get()
        self.ans_label2 = value

        if self.button["state"] == tk.NORMAL:
            self.button["state"] = tk.DISABLED
            self.button["bg"] = "grey"

        # 入力値の答え合わせ
        print("OKボタンを押しました")
        print(f"押した答え:{self.ans_label2},本当の答え：{self.ans}")
        if str(self.ans) == str(self.ans_label2):
            # logに書き込み
            log.logging(
                situation="集中",
                action="userがボタン入力",
                user_input=str(self.ans_label2),
                correct=str(self.ans),
                judge="正解",
                evaluation="-",
                eye_ans="-",
                ans_position="-",
                eye_correct="-",
                choice_1="-",
                choice_2="-",
                choice_3="-",
                choice_4="-",
            )

            self.result_label.configure(text="正解！", fg="red")
            self.correct_cnt += 1
        else:
            # logに書き込み
            log.logging(
                situation="集中",
                action="userがボタン入力",
                user_input=str(self.ans_label2),
                correct=str(self.ans),
                judge="不正解",
                evaluation="-",
                eye_ans="-",
                ans_position="-",
                eye_correct="-",
                choice_1="-",
                choice_2="-",
                choice_3="-",
                choice_4="-",
            )

            self.result_label.configure(text="残念！", fg="blue")

        # 次の問題を出題
        self.index += 1
        self.ans, q, radio_button_list = QUESTION()
        self.q_label2.configure(text=q)
        self.radio0.configure(
            text=str(radio_button_list[0]), value=str(radio_button_list[0])
        )
        self.radio1.configure(
            text=str(radio_button_list[1]), value=str(radio_button_list[1])
        )
        self.radio2.configure(
            text=str(radio_button_list[2]), value=str(radio_button_list[2])
        )
        self.radio3.configure(
            text=str(radio_button_list[3]), value=str(radio_button_list[3])
        )
        # "OK"のボタンを押したかどうか
        self.next = False

    def timer(self):
        self.second = 0
        self.flg = True
        while self.flg:
            self.second += 1
            self.time_label.configure(text=f"経過時間：{self.second}秒")
            time.sleep(1)

            # 2分経ったら
            if self.second == interval:
                # logに書き込み
                log.logging(
                    situation="計算課題の終了",
                    action="-",
                    user_input="-",
                    correct="-",
                    judge="-",
                    evaluation="-",
                    eye_ans="-",
                    ans_position="-",
                    eye_correct="-",
                    choice_1="-",
                    choice_2="-",
                    choice_3="-",
                    choice_4="-",
                )

                self.q_label2.configure(text="")
                messagebox.showinfo(
                    "リザルト",
                    f"あなたのスコアは{self.correct_cnt}/{self.index}問正解です。\nクリアタイムは{self.second}秒です。",
                )

                # logに書き込み
                # root.destroy()

                # quit_me(root)
                # sys.exit(0)
                self.second = 0
                self.destroy()
                self.master.destroy()

                global count
                count += 1
                questionnaire()
                return 0

"""
####言語課題####
class Language(tk.Frame):
    def __init__(self, master):
        # logに書き込み
        log.logging(
            situation="言語課題の説明",
            action="-",
            user_input="-",
            correct="-",
            judge="-",
            evaluation="-",
            eye_ans="-",
            ans_position="-",
            eye_correct="-",
            choice_1="-",
            choice_2="-",
            choice_3="-",
            choice_4="-",
        )

        super().__init__(master)
        self.pack()

        # 問題数インデックス
        self.index = 0

        # 正解数カウント用
        self.correct_cnt = 0


        # self.pack()
        self.column_data = (0, 0, 1, 1)
        self.row_data = (0, 1, 0, 1)
        # 各種ウィジェットの作成
        self.label1_frame_app = tk.Label(self.master, text="言語課題", font=("", 40))#,fg="red")
        self.label2_frame_app = tk.Label(self.master, text="4択のうち正しい答えを選択し決定してください", font=("", 40))
        self.label3_frame_app = tk.Label(self.master, text="1問あたり制限時間5秒で答えてください。全部で24問です。", font=("", 30))
        self.button_change_frame_app = tk.Button(
            self.master, text="課題に進む", font=("", 40), bg="grey", command=lambda: self.rocate(),relief="solid"
        )
        # 各種ウィジェットの設置
        self.label1_frame_app.pack(anchor="center", expand=1)
        self.label2_frame_app.pack(anchor="center", expand=1)
        self.label3_frame_app.pack(anchor="center", expand=1)
        self.button_change_frame_app.pack(anchor="center", expand=1)


    def rocate(self):
        # logに書き込み
        log.logging(
            situation="言語課題の説明",
            action="進むボタンを押した",
            user_input="-",
            correct="-",
            judge="-",
            evaluation="-",
            eye_ans="-",
            ans_position="-",
            eye_correct="-",
            choice_1="-",
            choice_2="-",
            choice_3="-",
            choice_4="-",
        )
        self.label1_frame_app.pack_forget()
        self.label2_frame_app.pack_forget()
        self.label3_frame_app.pack_forget()
        self.button_change_frame_app.pack_forget()
        self.create_widgets()

        # 経過時間スレッドの開始
        self.t = threading.Thread(target=self.timer, daemon=True)
        self.t.start()

        # Tkインスタンスに対してキーイベント処理を実装
        # self.master.bind("<KeyPress>", self.type_event)

    # ウィジェットの生成と配置
    def create_widgets(self):
        # logに書き込み
        log.logging(
            situation="言語課題の開始",
            action="-",
            user_input="-",
            correct="-",
            judge="-",
            evaluation="-",
            eye_ans="-",
            ans_position="-",
            eye_correct="-",
            choice_1="-",
            choice_2="-",
            choice_3="-",
            choice_4="-",
        )

        # # 時間計測用のラベル
        self.time_label = tk.Label(self, text="", font=("", 20))
        self.time_label.grid(row=0, column=0, columnspan=3)

        self.ans_label2 = tk.Label(self, text="", width=10, anchor="w", font=("", 40))
        self.ans_label2.grid(row=2, column=0)

        # 問題作成
        self.ans, self.q, self.radio_button_list, self.genre = question_language(self.index)

        self.q_label2 = tk.Label(self, text="Q.下の単語と", font=("", 30))
        self.q_label2.grid(row=3, column=0)
        self.q_label = tk.Label(self, text=self.genre, font=("", 30), fg="red")
        self.q_label.grid(row=3, column=1)
        self.q_label1 = tk.Label(self, text="   を選択してください。", font=("", 30))
        self.q_label1.grid(row=3, column=2)
        self.ans_label3 = tk.Label(self, text="", width=10, anchor="w", font=("", 15))
        self.ans_label3.grid(row=4, column=0)
        self.q_label2 = tk.Label(self, text=self.q, width=10, font=("", 50, "bold"))
        self.q_label2.grid(row=5, column=0,columnspan=3)


        # ウィジェットの作成
        self.radio_value = tk.IntVar()  # ラジオボタンの初期値を0にする
        self.radio_value.set(4)

        # ラジオボタンの作成
        self.radio0 = tk.Radiobutton(
            self.master,
            text=str(self.radio_button_list[0]),  # ラジオボタンの表示名
            command=self.radio_click,  # クリックされたときに呼ばれるメソッド
            variable=self.radio_value,  # 選択の状態を設定する
            value=0,  # ラジオボタンに割り付ける値の設定
            indicator=0,
            background="light blue",
            font=("", 20),
            width=20,
            height=3,
        )

        self.radio1 = tk.Radiobutton(
            self.master,
            text=str(self.radio_button_list[1]),  # ラジオボタンの表示名
            command=self.radio_click,  # クリックされたときに呼ばれるメソッド
            variable=self.radio_value,  # 選択の状態を設定する
            value=1,  # ラジオボタンに割り付ける値の設定
            indicator=0,
            background="light blue",
            font=("", 20),
            width=20,
            height=3,
        )

        self.radio2 = tk.Radiobutton(
            self.master,
            text=str(self.radio_button_list[2]),  # ラジオボタンの表示名
            command=self.radio_click,  # クリックされたときに呼ばれるメソッド
            variable=self.radio_value,  # 選択の状態を設定する
            value=2,  # ラジオボタンに割り付ける値の設定
            indicator=0,
            background="light blue",
            font=("", 20),
            width=20,
            height=3,
        )

        # ウィジェットの設置
        self.radio0.pack()
        self.radio1.pack()
        self.radio2.pack()

        self.result_label = tk.Label(self, text="", font=("", 20))
        self.result_label.grid(row=6, column=0, columnspan=3)
        self.ans_label3 = tk.Label(self, text="", width=10, anchor="w", font=("", 30))
        self.ans_label3.grid(row=7, column=0)

        self.question_label1 = tk.Label(self, text="回答数:"+ str(self.index+1) +"/24", font=("", 20))
        self.question_label1.grid(row=1, column=0, columnspan=3)

        self.flg2 = True

    def radio_click(self):
        # ラジオボタンの値を取得
        value = self.radio_value.get()
        print(f"ラジオボタンの値は {self.radio_button_list[value]} です")

        # "OK"のボタンを押したかどうか
        self.next = False


    def timer(self):
        self.second = 0
        self.flg = True
        while self.flg:
            self.second += 1
            self.time_label.configure(text=f"経過時間：{self.second}秒")
            time.sleep(1)

            if self.second == 5:
                global log
                value = self.radio_value.get()
                self.ans_label2 = value

                print(f"押した答え:{self.ans_label2},本当の答え：{self.ans}")
                if self.ans_label2 == 4:
                    # logに書き込み
                    log.logging(
                        situation="集中",
                        action="問題遷移",
                        user_input="無回答",
                        correct=str(self.ans),
                        judge="不正解",
                        evaluation="-",
                        eye_ans="-",
                        ans_position="-",
                        eye_correct="-",
                        choice_1="-",
                        choice_2="-",
                        choice_3="-",
                        choice_4="-"
                    )
                elif str(self.ans) == str(self.radio_button_list[self.ans_label2]):
                    # logに書き込み
                    log.logging(
                        situation="集中",
                        action="問題遷移",
                        user_input=str(self.radio_button_list[self.ans_label2]),
                        correct=str(self.ans),
                        judge="正解",
                        evaluation="-",
                        eye_ans="-",
                        ans_position="-",
                        eye_correct="-",
                        choice_1="-",
                        choice_2="-",
                        choice_3="-",
                        choice_4="-",
                    )

                    self.result_label.configure(text="正解！", fg="red")
                    self.correct_cnt += 1
                else:
                    # logに書き込み
                    log.logging(
                        situation="集中",
                        action="問題遷移",
                        user_input=str(self.radio_button_list[self.ans_label2]),
                        correct=str(self.ans),
                        judge="不正解",
                        evaluation="-",
                        eye_ans="-",
                        ans_position="-",
                        eye_correct="-",
                        choice_1="-",
                        choice_2="-",
                        choice_3="-",
                        choice_4="-",
                    )

                    self.result_label.configure(text="残念！", fg="blue")

                # 次の問題を出題
                self.index += 1
                print(self.index)
                if self.index == 24:
                    # logに書き込み
                    log.logging(
                        situation="計算課題の終了",
                        action="-",
                        user_input="-",
                        correct="-",
                        judge="-",
                        evaluation="-",
                        eye_ans="-",
                        ans_position="-",
                        eye_correct="-",
                        choice_1="-",
                        choice_2="-",
                        choice_3="-",
                        choice_4="-",
                    )

                    self.q_label2.configure(text="")
                    messagebox.showinfo(
                        "リザルト",
                        f"あなたのスコアは{self.correct_cnt}/{self.index}問正解です。",
                    )

                    self.second = 0
                    self.destroy()
                    self.master.destroy()

                    global count
                    count += 1
                    questionnaire()
                    return 0

                self.ans, self.q, self.radio_button_list, self.genre = question_language(self.index)
                self.q_label2.configure(text=self.q)
                self.radio_value.set(4)

                if self.genre == "似た意味の単語":
                    self.q_label.configure(text=self.genre, fg="red")
                else:
                    self.q_label.configure(text=self.genre, fg="blue")

                self.radio0.configure(
                    text=str(self.radio_button_list[0]), variable = self.radio_value
                )
                self.radio1.configure(
                    text=str(self.radio_button_list[1]), variable = self.radio_value
                )
                self.radio2.configure(
                    text=str(self.radio_button_list[2]), variable = self.radio_value
                )
                self.question_label1.configure(text="回答数:"+ str(self.index+1) +"/24")
                self.second = 0


# log
class Log:
    def first_log(self, first_time):
        self.first_time = first_time

    def logging(
            self, situation: str, action: str, user_input: str, correct: str, judge: str, evaluation: str, eye_ans: str, ans_position: str, eye_correct: str,
            choice_1: str, choice_2: str, choice_3: str, choice_4: str,
    ):
        self.situation = situation
        self.action = action
        self.user_input = user_input
        self.correct = correct
        self.judge = judge
        self.evaluation = evaluation
        self.eye_ans = eye_ans
        self.ans_position = ans_position
        self.eye_correct = eye_correct
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3
        self.choice_4 = choice_4

        filepath = f".\\log_dir\\{self.first_time}.csv"
        columns = ["時間", "状態", "アクション", "計算課題の入力", "正解値", "正誤判定","集中度自己評価","視線課題の入力","答えの位置","正解","第1象限","第2象限","第3象限","第4象限"]

        dt_now = datetime.datetime.now()
        time = dt_now.strftime('%Y_%m_%d_%H.%M.%S')
        print(time)
        # self.log_data = {
        #     "time": [],
        #     "situation": [],
        #     "action": [],
        #     "user_input": [],
        #     "correct": [],
        #     "judge": [],
        # }
        self.log_data = {
            "時間": [],
            "状態": [],
            "アクション": [],
            "計算課題の入力": [],
            "正解値": [],
            "正誤判定": [],
            "集中度自己評価": [],
            "視線課題の入力": [],
            "答えの位置": [],
            "正解": [],
            "第1象限": [],
            "第2象限": [],
            "第3象限": [],
            "第4象限": [],
        }
        # self.log_data["time"].append(time)
        # self.log_data["situation"].append(self.situation)
        # self.log_data["action"].append(self.action)
        # self.log_data["user_input"].append(self.user_input)
        # self.log_data["correct"].append(self.correct)
        # self.log_data["judge"].append(self.judge)

        self.log_data["時間"].append(time)
        self.log_data["状態"].append(self.situation)
        self.log_data["アクション"].append(self.action)
        self.log_data["計算課題の入力"].append(self.user_input)
        self.log_data["正解値"].append(self.correct)
        self.log_data["正誤判定"].append(self.judge)
        self.log_data["集中度自己評価"].append(self.evaluation)
        self.log_data["視線課題の入力"].append(self.eye_ans)
        self.log_data["答えの位置"].append(self.ans_position)
        self.log_data["正解"].append(self.eye_correct)
        self.log_data["第1象限"].append(self.choice_1)
        self.log_data["第2象限"].append(self.choice_2)
        self.log_data["第3象限"].append(self.choice_3)
        self.log_data["第4象限"].append(self.choice_4)

        if os.path.isfile(filepath):
            df1 = pd.read_csv(filepath, encoding="shift_jis")
            df2 = pd.DataFrame(self.log_data)
            df = pd.merge(df1, df2, how="outer")
            df.to_csv(
                filepath,
                encoding="shift_jis",
                index=False,
            )
        else:
            df = pd.DataFrame(self.log_data)
            df.to_csv(
                filepath,
                encoding="shift_jis",
                index=False,
                columns=columns
            )


if __name__ == "__main__":
    root = tk.Tk()
    # root.geometry("1280x720")
    # root.state("zoomed")
    global count
    count = 1
    root.attributes("-fullscreen", True)
    root.title("タイピングゲーム！")

    dt_now = datetime.datetime.now()
    now = dt_now.strftime('%Y_%m_%d_%H.%M.%S')[:-3]
    global log
    log = Log()
    log.first_log(now)
    # logに書き込み
    log.logging(situation="課題スタート", action="-", user_input="-", correct="-", judge="-", evaluation="-", eye_ans="-",ans_position="-", eye_correct="-",
                choice_1="-", choice_2="-", choice_3="-", choice_4="-")
    #print("A:"+datetime.datetime.now().strftime('%Y_%m_%d_%H.%M.%S.%f')[:-3])

    # log.log_to_csv()

    change()  # シーン変更先
    # change(eye_task)
    root.protocol("WM_DELETE_WINDOW", click_close)
    root.mainloop()
# https://max999blog.com/pandas-add-row-to-dataframe/