from proven.comprescistella.views.Option import Option
from proven.comprescistella.views.Menu import Menu


class CCMenu(Menu):
    
    def __init__(self):
        super().__init__("--COMPRA CISTELLA MENU--")
        self.addOption(Option("Exit", "exit"))
        self.addOption(Option("Identificació", "identificacio"))
        self.addOption(Option("Registrarse", "registrarse"))
    
    def canviMenu(self):
        self.removeOption(Option("Identificació", "identificacio"))
        self.removeOption(Option("Registrarse", "registrarse"))
        self.addOption(Option("Comprar un producte", "comprar_producte"))
        self.addOption(Option("Mostrar cistella de compra", "mostrar_cistella"))
        self.addOption(Option("Generar factura", "generar_factura"))