from tkinter import *
import tkinter.font
from tkinter import messagebox
from onmt.bin.translate import main
import sentencepiece as spm

def Korean_tokenizer(x):
    sp = spm.SentencePieceProcessor()
    sp.Load('data/korean_tok.model')
    tokens = []
    for words in x:
        token=sp.EncodeAsPieces(words)
        b=[]
        for word in token:
            c = word.replace("▁", "")
            if c != '':
                b.append(c)
        tokens.append(" ".join(b))
    return tokens

class main2:
    def __init__(self,window):
        self.window = window
        self.window.title("Kwangwoon Univ. Capstone Project (TEAM YOUNGILE Translator)")
        self.window.geometry("870x500+500+250")
        self.window.configure(bg="SlateGray1")
        self.window.resizable(False, False)
        self.transInput()

        icon = PhotoImage(file='icon.png')
        self.window.iconphoto(False, icon)


    def transInput(self):

        self.font = tkinter.font.Font(family="나눔스퀘어 ExtraBold", size=25)
        self.font1 = tkinter.font.Font(family="나눔스퀘어 Bold", size=15)
        self.font2 = tkinter.font.Font(family="나눔스퀘어 Regular", size=11)
        self.font3 = tkinter.font.Font(family="나눔스퀘어라운드 Light", size=9)
        self.bg = "SlateGray1"
        self.bg2 = "SlateGray3"
        self.bg3 = "SlateGray2"
        self.bg4 = "DodgerBlue2"
        self.bg5 = "gray50"

        self.f0 = Frame(self.window, height=10)
        self.f0.grid(row=0, column=0)
        self.f0.configure(bg=self.bg)
        self.f0 = Frame(self.window, height=75)
        self.f0.grid(row=1, column=0)
        self.f0.configure(bg=self.bg)
        self.f01 = Frame(self.window, width=25)
        self.f01.grid(row=2, column=0)
        self.f01.configure(bg=self.bg)
        self.f02 = Frame(self.window, width=8, padx=23)
        self.f02.grid(row=4, column=2)
        self.f02.configure(bg=self.bg)
        self.f03 = Frame(self.window, height=60, pady=0)
        self.f03.grid(row=1, column=1)
        self.f03.configure(bg=self.bg)
        self.f04 = Frame(self.window, height=10, pady=5)
        self.f04.grid(row=2, column=1)
        self.f04.configure(bg=self.bg)

        self.f1 = Frame(self.window, height=400, bd=1, pady=20)
        self.f1.grid(row=4, column=1)
        self.f1.configure(bg=self.bg)
        self.f2 = Frame(self.window, height=400, bd=1, pady=20)
        self.f2.grid(row=4, column=3)
        self.f2.configure(bg=self.bg)

        arrow = PhotoImage(file="right-arrow.png")
        self.l0 = Label(self.f02, image=arrow, height=40, bg=self.bg)
        self.l0.image = arrow
        self.l0.grid(row=0, column=0, padx=0)

        self.l3 = Label(self.window, text="딥러닝 기반 한-영 기계번역", anchor='center', font=self.font, bg=self.bg)
        self.l3.place(x=250, y=20, width=400, height=40)
        self.l3 = Label(self.window, text="Developed by Team Youngile", fg='grey29', anchor='center', font=self.font3, bg=self.bg)
        self.l3.place(x=290, y=60, width=300, height=40)

        self.l1 = Label(self.f1, text="한국어", font=self.font1, width=30, pady=1)
        self.l1.grid(row=0, column=0)
        self.l1.configure(bg=self.bg3)
        self.tb1 = Text(self.f1, width=50, padx=6, pady=5, wrap="word")
        self.tb1.grid(row=1, column=0)
        self.sl1 = Scrollbar(self.f1)
        self.sl1.grid(row=1, column=0,sticky=N+S+E)
        self.sl1.config(command=self.tb1.yview)
        self.tb1.config(yscrollcommand=self.sl1.set)

        self.l2 = Label(self.f2, text="영어", font=self.font1, width=30, pady=1)
        self.l2.grid(row=0, column=0)
        self.l2.configure(bg=self.bg3)
        self.tb2 = Text(self.f2, width=50, padx=6, pady=5, wrap="word")
        self.tb2.grid(row=1, column=0)
        self.sl2 = Scrollbar(self.f2)
        self.sl2.grid(row=1, column=0, sticky=N+S+E)
        self.sl2.config(command=self.tb2.yview)
        self.tb2.config(yscrollcommand=self.sl2.set)

        self.tran=Button(self.window, text="번역하기", font=self.font2, fg="snow", command=self.trans, bg=self.bg4)
        self.tran.place(x=403, y=350, width=70, height=40)

        self.delete=Button(self.window, text="새로고침", font=self.font2, fg="snow", command=self.deleteText, bg=self.bg5)
        self.delete.place(x=403, y=410, width=70, height=40)

    def deleteText(self):
        self.getText(0)
        self.tb1.delete(1.0, "end")
        self.tb2.delete(1.0, "end")

    def getText(self, num):
        if num == 0:
            self.result1 = self.tb1.get("1.0", "end")
            self.result2 = self.tb2.get("1.0", "end")
        elif num == 1:
            self.result1 = self.tb1.get("1.0", "end")
            return self.result1
        elif num == 2:
            self.result2 = self.tb2.get("1.0", "end")
            return self.result2

    def isChar(self):
        result = self.getText(1)
        ischar = 1
        for word in result.strip():
            if not self.isHangulOrSymbol(word):
                ischar = 0
        if ischar == 0:
            messagebox.showinfo("Warning message", "알 수 없는 문자가 포함되어 있습니다. \n다시 시도해주세요.")
        return ischar

    def isHangulOrSymbol(self, text):
        hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
        symbolList = [' ', '.', '?', '!', '~', '\n']
        if text in symbolList:
            hanCount = hanCount + 1
        return hanCount > 0

    def trans(self):
        if self.isChar():
            with open("data/demo/input.txt", "w+", encoding='utf-8') as f:
                f.write(self.tb1.get('1.0', 'end'))
            with open("data/demo/input.txt", "r", encoding='utf-8') as f:
                line=f.readlines()

            token = Korean_tokenizer(line)
            with open("data/demo/koreanTokenInput.txt", "w", encoding='utf-8') as f:
                for row in token:
                    if row == '':
                        pass
                    else:
                        f.write(row)
                        f.write('\n')

            main()
            f = open("data/demo/EnglishTokenOutput.txt", 'r', encoding="utf-8")
            line = f.read()
            print(line)
            f.close()
            self.tb2.delete('1.0', 'end')
            self.tb2.insert(1.0, line)


window=Tk()
main2(window)
window.mainloop()
