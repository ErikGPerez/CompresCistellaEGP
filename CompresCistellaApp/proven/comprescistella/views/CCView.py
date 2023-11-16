from CompresCistellaApp.proven.comprescistella.views.CCMenu import CCMenu
from CompresCistellaApp.proven.comprescistella.model.CCModel import CCMenu
from CompresCistellaApp.proven.comprescistella.controllers.CCController import *

class CCView:
    def __init__(self, control, model):
        self.control = control
        self.model = model
        self.menu = CCMenu()
    
    def showInputDialog(self, message):
        print(message)
        return input()
    
    def showMessage(self, message):
        print(message)
        
    def display(self):
        while True:
            self.menu.show()
            action = self.menu.getSelectedOptionActionCommand()
            self.processAction(action)
            
            
    def processAction(self, action):
        if action != None:
            if action:
                self.control.processRequest(action)
    
    def showTable(self, data):
        cont = 0
        for Object in data:
            print(Object)
            cont = cont + 1
        print(str(cont) + " Elements found")
        
    def crudForm(self, inputU):
        return inputU