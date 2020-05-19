from tkinter import *
import tkinter.messagebox
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
        self.window.title("한영 번역기")
        self.window.resizable(False, False)
        self.transInput()

    def transInput(self):
        self.f1 = Frame(self.window, height=400)
        self.f1.grid(row=0, column=0)
        self.f2 = Frame(self.window, height=400)
        self.f2.grid(row=0, column=1)
        self.f3 = Frame(self.window, height=100)
        self.f3.grid(row=1, column=0, columnspan=2)

        self.l1 = Label(self.f1, text="[ 한글 ]", font=("맑은 고딕", 15,"bold"), width=30)
        self.l1.grid(row=0, column=0, pady=10)
        self.tb1 = Text(self.f1, width=40, wrap="word")
        self.tb1.grid(row=1, column=0)
        self.sl1 = Scrollbar(self.f1)
        self.sl1.grid(row=1, column=1,sticky=N+S+W)
        self.sl1.config(command=self.tb1.yview)
        self.tb1.config(yscrollcommand=self.sl1.set)


        self.l2 = Label(self.f2, text="[ 영어 ]", font=("맑은 고딕", 15,"bold"), width=30)
        self.l2.grid(row=0, column=0, pady=10)
        self.tb2 = Text(self.f2, width=40, wrap="word")
        self.tb2.grid(row=1, column=0)
        self.sl2 = Scrollbar(self.f2)
        self.sl2.grid(row=1, column=1, sticky=N + S+W)
        self.sl2.config(command=self.tb2.yview)
        self.tb2.config(yscrollcommand=self.sl2.set)

        self.tran=Button(self.f3, text="번역", command=self.trans)
        self.tran.pack(pady=10)

    def isHangul(self, text):
        hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
        return hanCount > 0

    def trans(self):
        '''
        if self.isHangul(self.tb1.get('1.0', 'end')):
            f = open("data/demo/koreanInput.txt", 'w', encoding="utf-8")
            a=Korean_tokenizer(self.tb1.get('1.0', 'end'))
            f.write(self.tb1.get('1.0', 'end'))
            f.close()
            main()
            f = open("data/demo/englishPred.txt", 'r')
            line=f.read()
            f.close()
            self.tb2.delete('1.0', 'end')
            self.tb2.insert(1.0,line)
        else:
            tkinter.messagebox.showwarning("입력","다시 입력하세요.")
        '''
        with open("data/demo/Input.txt", "w+", encoding='utf-8') as f:
            f.write(self.tb1.get('1.0', 'end'))
        with open("data/demo/Input.txt", "r", encoding='utf-8') as f:
            line=f.readlines()

        token = Korean_tokenizer(line)
        with open("data/demo/koreanTokenInput.txt", "w", encoding='utf-8') as f:
            for row in token:
                f.write(row)
                f.write('\n')

        main()
        f = open("pred.txt", 'r', encoding="utf-8")
        line = f.read()
        f.close()
        self.tb2.delete('1.0', 'end')
        self.tb2.insert(1.0, line)


window=Tk()
main2(window)
window.mainloop()
