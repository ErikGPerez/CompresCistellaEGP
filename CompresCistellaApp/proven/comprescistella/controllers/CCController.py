from proven.comprescistella.views.CCView import CCView
from proven.comprescistella.model.CCModel import CCModel

class CCController:
    
    def __init__(self, model: CCModel):
        self.model = model
        self.view = CCView(self, self.model)
        self.view.display()
        
    def processRequest(self, action):
        """Requests the process of what action choosed the user

        Args:
            action (str): Given action by the user
        """
        if action == None:
            action = "wrong_action"
        else:
            if action == "exit":
                self.exitApplication()
            if action == "identificacio":
                self.identificacioUser()
            if action == "registrarse":
                self.registreUser()
            if action == "comprar_producte":
                self.compraProducte()
            if action == "mostrar_cistella":
                self.mostraCistella()
            if action == "generar_factura":
                self.generaFactura()
            if action == "wrong_action":
                print("Wrong option")
    
    def exitApplication(self):
        """Quit the programm
        """
        quit()
    
    #### MENU USER ####

    def identificacioUser(self):
        """Identifies an user on the file uspass.txt inside the folder data
        """
        usuari = self.view.showInputDialog("Usuari: ")
        password = self.view.showInputDialog("Password: ")
        
        uspass = self.model.readFileUser()
        
        if uspass != "File not found":
            if self.model.checkUser(usuari, password, uspass):
                self.model.loadProducts()
                self.view.subMenu()
            else:
                self.view.showMessage("User and password not found!")
    
    def registreUser(self):
        """Register a new user on the file uspass.txt inside the folder data
        """
        self.view.showMessage("--Fes el registre d'usuari--")
        usuari = self.view.showInputDialog("Usuari: ")
        password = self.view.showInputDialog("Password: ")
        
        if self.model.registerFileUser(usuari, password):
            self.view.showMessage("T'has registrat!")
        else:
            self.view.showMessage("No t'has registrat")
    
    #### MENU CISTELLA ####
    
    def compraProducte(self):
        """Buys a product. First, shows to user all the products. Then, user tries to
        input a number id to choose a product. If valid, adds to the basket. Otherwise, does nothing.
        """
        self.view.showMessage("--COMPRA UN PRODUCTE--")
        listPr = self.model.showProducts()
        count = 0
        for p in listPr:
            self.view.showMessage("[" + str(count) + "] " + p.mostraProducte())
            count += 1
        option = self.view.showInputDialog("Quin producte vols?: ([number] or [quit])")    
        if option != "quit":
            try:
                optionN = int(option)
                self.model.addBasket(listPr[optionN])
            except: 
                self.view.showMessage("Error en la entrada de la opció")
        
    def mostraCistella(self):
        """Shows the basket with a list of the products
        """
        self.view.showMessage(self.model.showBasket())
    
    def generaFactura(self):
        """Generates a bill on the data folder
        """
        self.view.showMessage("Generant Factura...")
        if self.model.generateBill():
            self.view.showMessage("Factura generada")
        else:
            self.view.showMessage("Factura no generada")
        
        opt = self.view.showInputDialog("Vols esborrar la cistella actual?: (y/n)")
        if opt == "y":
            self.model.removeCistella()
        