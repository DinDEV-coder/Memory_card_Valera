from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QButtonGroup
)
from random import shuffle,choice

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question 
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

        
 
 
def show_question():
    btn_OK.setText("Відповісти")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    RadioGroupBox.show()
    AnsGroupBox.hide()
 
 
def show_result():
    btn_OK.setText("Наступне питання")
    RadioGroupBox.hide()
    AnsGroupBox.show()
 
 
def ask(q):
    shuffle(answers)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    lb_Result.setText("???")
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)


def check_answer():
    if answers[0].isChecked():
        lb_Result.setText('Вірно')
        window.score +=1
    else:
        lb_Result.setText('Неправільно')
    print('Всього було задано запитань:',window.total)
    print('Всього правильних відповідей:',window.score)
    print("Рейтинг гравця:", (window.score / window.total) * 100, "%")
    show_result()

 
def start_test():
    btn_napis = btn_OK.text()
    if btn_napis == "Відповісти" :
        check_answer()
    else:
        next_question()
        show_question()

def next_question():
    window.total+=1
    question =choice(question_list)
    ask(question)
 
 
app = QApplication([]) # наш додаток
 
 
 
 
btn_OK = QPushButton('Відповісти') # кнопка для відповіді
lb_Question = QLabel("Very difficult Question:") # текст зі змістом запитання
 
 
 
 
RadioGroupBox = QGroupBox("Answer options:") # група кнопок відповідей
rbtn_1 = QRadioButton("Option 1") # кнопка відповіді 1
rbtn_2 = QRadioButton("Option 2") # кнопка відповіді 2
rbtn_3 = QRadioButton("Option 3") # кнопка відповіді 3
rbtn_4 = QRadioButton("Option 4") # кнопка відповіді 4
 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 
 
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
 
 
 
layout_ans1 = QHBoxLayout() #горизонталь варіантів відповідей
layout_ans2 = QVBoxLayout() #вертикаль 1 та 2 відповідь
layout_ans3 = QVBoxLayout() #вертикаль 3 та 4 відповідь
 
 
 
 
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
 
 
 
 
layout_line1 = QHBoxLayout()  #горизонталь з питанням
layout_line2 = QHBoxLayout()  #горизонталь з варіантами відповідей
layout_line3 = QHBoxLayout()  #горизонталь з кнопкою відповідь
 
 
 
 
AnsGroupBox = QGroupBox("Test Result")
lb_Result = QLabel("Correct / Incorrect")
lb_Correct = QLabel("Correct answer")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
 
 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
 
 
 
 
 
 
layout_card = QVBoxLayout() #головний вертикальний макет
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=1)
 
 
RadioGroupBox.show()
AnsGroupBox.hide()
 
 
btn_OK.clicked.connect(start_test)
 
question_list=[]
question_list.append(Question(
    "Якого кольору Valera?",
    "Червоного",
    "Синього",
    "Жовтого",
    "Білого"
))

question_list.append(Question( 
    "Про що YouTube шоу Valera?",
    "Про експерименти",
    "Про країни",
    "Про покемонів",
    "Про їжу"
))

question_list.append(Question(
    "Медвідь Валера із чого зроблений",
    "З желе",
    "З метала",
    "З борошна",
    "З листях",
))
question_list.append(Question(
    "Яка форма у Валери",
    "Медвідня",
    "Кругла",
    "Квадратна",
    "Овальна"
))

question_list.append(Question(
    "Есть у Валери Друг",
    "Нету він один",
    "Друг Жолтобрух", 
    "Друг Паша",
    "Валера не друже з Жолтобрухом только с Пашей",
))

window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(500, 300)
window.setLayout(layout_card)
window.total=0
window.score=0
next_question()

window.show()
app.exec()
