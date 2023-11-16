from CompresCistellaApp.proven.comprescistella.model.CCModel import CCMenu
from CompresCistellaApp.proven.comprescistella.controllers.CCController import CCController

##Init main to run programm
class Main:
    def __init__(self):
        model = CCMenu()
        control = CCController(model)

main = Main()
    