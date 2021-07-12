from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication , QMainWindow
from v1 import Ui_MainWindow
import sys
import os
import json
import bot

class F0(QMainWindow):

        def __init__(self):

            self.chat_log = ""
            self.tag_quesion_answer_list = []

            super(F0, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.q.setFocus()

            self.ui.s.clicked.connect(self.btnClickeds)
            self.ui.ab.clicked.connect(self.btnClickedab)
            self.ui.tr.clicked.connect(self.btnClickedtr)
            self.ui.ad.clicked.connect(self.btnClickedad)

            #self.ui.qb.setPlaceholderText('choose topic')
            self.update_combo_Box()

        def update_combo_Box(self):

            with open('intents.json', 'r') as f:
                intents = json.load(f)
            tag_names = []
            for dic in intents['intents']:
                tag_names.append(dic["tag"])

            self.ui.qb.addItems(tag_names)


        def btnClickeds(self):
            s = self.ui.q.toPlainText()
            self.chat_log += s
            self.chat_log += "\n"
            self.chat_log += bot.chatbot_response(s) + "\n"
            self.ui.dis.setPlainText(self.chat_log)
            self.ui.q.clear()
            self.ui.q.setFocus()

        def btnClickedab(self):
            tag = self.ui.qb.currentText()                  #
            print("tag name is: ", tag)                     #
            q = self.ui.qu.text()                           #
            print("question is: ", q)                       #
            a = self.ui.an.text()                           #
            print("answer is: ", a)                         #

            self.tag_quesion_answer_list.append([tag, q, a])        #
            print(self.tag_quesion_answer_list)                     #

            #self.ui.qb.setCurrentText("choose topic")           # didn't work and clear also didn't work
            self.ui.qu.clear()                              #
            self.ui.an.clear()  

        def btnClickedtr(self):
            pass
            # loop trough each element of the self.tag_quesion_answer_list and 
            # put the qustions and answer of under each corrosponding tag
            # after finishing run the script that trains the module
            with open('intents.json') as json_file: 
                data = json.load(json_file)
                temp = data['intents']
                for each_list in self.tag_quesion_answer_list:    
                    for item in temp:
                        if item["tag"] == each_list[0]:
                            item["patterns"].append(each_list[1])
                            item["responses"].append(each_list[2])
                with open("intents.json",'w') as f: 
                    json.dump(data, f)
            os.system('cmd/c "py train_chatbot.py"')
            f_0.hide()
            os.system('cmd/c "py main.py"')
            

        def btnClickedad(self):
            # append a new tag into the intents.json
            new_tag = self.ui.nt.text()
            x = {"tag": new_tag, "patterns": [], "responses": [], "context": [""]}
            with open('intents.json') as json_file: 
                data = json.load(json_file)
                temp = data['intents']
                for item in temp:
                    if item["tag"] == x["tag"]:
                        print("this topic already exists")
                        return
                temp.append(x)
            with open("intents.json",'w') as f: 
                json.dump(data, f)
            self.update_combo_Box()



app = QApplication([])
f_0 = F0()
f_0.show()
sys.exit(app.exec())
