import json as js

f = open("praktyki/062021/lukasz_sedkowski/repo/quiz/quiz.json", "rt")
quest = js.loads(f.read())
f.close()

choice_qst=int(input("wybierz nr pytania od 1 do 3: "))
choice_qst-=1
qst_one = quest[choice_qst]
print(qst_one["question"])

ans = qst_one["answers"]
x=0

while x < 4 :
    print(ans[x])
    x+=1

cor_ans=input("Podaj nr od 1 do 4: ")

if int(cor_ans) == int(qst_one["correct_answer"]):
    print("No i gitara")
else:
    print("Unlucky, better luck next time :(")
