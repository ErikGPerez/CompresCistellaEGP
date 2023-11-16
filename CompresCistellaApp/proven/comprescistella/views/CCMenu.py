from proven.comprescistella.views.Option import Option
from proven.comprescistella.views.Menu import Menu


class CCMenu(Menu):
    
    def __init__(self):
        super().__init__("--COMPRA CISTELLA MENU--")
        self.addOption(Option("Exit", "exit"))
        self.addOption(Option("Crear fitxer", "crear_fitxer"))
        self.addOption(Option("Llegir fitxer", "llegir_fitxer"))
        self.addOption(Option("Escriure fitxer", "escriure_fitxer"))
        self.addOption(Option("Esborrar fitxer", "esborrar_fitxer"))
        