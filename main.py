import ast
from PyQt5 import QtWidgets, uic
import sys

class main:
   automata = ""
   rastreo = ""
   list_rechazados = []
   list_aceptados = []

 
   def init_dfa(self,automata,w):
      return self.run_fda(automata,w) in automata["F"]
         
   def final_dfa(self,automata,q,a):
      try:
         assert(a in automata["Sigma"])
         assert(q in automata["Q"])
         return automata["Delta"][(q,a)]
      except:
         return False
      
   def dfa_very(self,automata,w,q):
      if w == "":
         return q
      else:
         return self.dfa_very(automata,w[1:], self.final_dfa(automata,q,w[0]))
      
   def run_fda(self,automata,w):
      curstate = automata["q0"]
      if w == "":
         return curstate
      
      return self.dfa_very(automata,w[1:], self.final_dfa(automata,curstate,w[0]))
   
   
   def readFile(self,filename):
      try:
         with open(filename, 'r', encoding='utf-8') as file:
            if "Codigos" in filename:
               content = file.read().split('\n')
               return content
            else:
               content = file.read()
         self.automata = ast.literal_eval(content)
      except Exception as e:
         print(f"El archivo '{filename}' no existe.") 
         
   def selectFile(self):
      filename = QtWidgets.QFileDialog.getOpenFileName(None, "Abrir archivo", "", "Text files (*.txt)")
      self.rastreo = self.readFile(filename[0])   

   def main(self,UI):
      for dir in self.rastreo:
         if self.init_dfa(self.automata, dir):

            self.list_aceptados.append(dir)
         else:
            self.list_rechazados.append(dir)
            
      UI.list_result.addItems(self.list_aceptados)
      UI.list_result_1.addItems(self.list_rechazados)
      
   

      
      
if __name__ == "__main__":   
   app = QtWidgets.QApplication(sys.argv)
   UI = uic.loadUi("interfaz.ui")
   UI.show()
   main = main()
   
   main.readFile("automata.txt")
   
   UI.selectFile.clicked.connect(main.selectFile)
   
   UI.evaluate_test.clicked.connect(lambda: main.main(UI))
  
   
   
   
   sys.exit(app.exec_())
   
   
   

   
   