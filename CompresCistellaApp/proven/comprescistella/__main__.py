from proven.comprescistella.model.CCModel import CCModel
from proven.comprescistella.controllers.CCController import CCController

##Init main to run programm
class Main:
    def __init__(self):
        model = CCModel()
        control = CCController(model)

main = Main()