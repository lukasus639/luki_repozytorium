import json as js

class Quest:
    def __init__(self, pyt_load):
        self.pyt = pyt_load
        self.qus = self.pyt['question']
        self.answ = self.pyt['answers']
        self.cor_answ = self.pyt['correct_answer']


    def quest(self):
        print(self.qus)

        
    def answer(self):
        i = 0
        while i < len(self.answ):
            print(self.answ[i])
            i+=1

    def correct_answ(self):
        self.cor_answ=str(self.cor_answ)
        if self.cor_answ == input(str("Podaj odpowiedź ")):
            
            print("No i gitara ")
        else:
            print("Unlucky")

def js_load(path):
    f = open("praktyki/062021/lukasz_sedkowski/repo/quiz/" + path)
    quest = js.loads(f.read())
    f.close()
    return quest

call = js_load("quiz.json")

call = [Quest(call[questions]) for questions in range(len(call))]


usercall=int(input("podaj numer pytania od 0 do 3: "))

str(call[usercall].quest())
call[usercall].answer()
str(call[usercall].correct_answ())



