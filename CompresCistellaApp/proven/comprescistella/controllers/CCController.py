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
        usuari = self.view.showInputDialog("Usuari: ")
        password = self.view.showInputDialog("Password: ")
        
        user = self.model.readFileUser()
        self.view.showMessage(user)
        
        if user != "File not found":
            self.view.subMenu()
    
    def registreUser(self):
        self.view.showMessage("NOT IMPLEMENTED cistella") #TODO  
        self.view.subMenu()  
    
    
    
    #### MENU CISTELLA ####
    
    def compraProducte(self):
        self.view.showMessage("NOT IMPLEMENTED compra") #TODO
        self.model.prova()
        
    def mostraCistella(self):
        self.view.showMessage("NOT IMPLEMENTED cistella") #TODO
    
    def generaFactura(self):
        self.view.showMessage("NOT IMPLEMENTED genera") #TODO
    
    ############################# OTHER ACTIVITY - CRUD #######################
    
    def crearFitxer(self):
        """Creates a file next to __main__.py asking the name to the user
        """
        filepath = self.view.showInputDialog("Nom del nou arxiu: ")
        if self.model.createFile(filepath):
            self.view.showMessage("L'arxiu " + filepath + " s'ha creat correctament")
        else:
            self.view.showMessage("L'arxiu " + filepath + " no s'ha creat")
            
    def llegirFitxer(self):
        """Reads a file using File object giving the filepath to the model and returning the String
        """
        filepath = self.view.showInputDialog("Nom del arxiu a llegir: ")
        fileRead = self.model.readFile(filepath)
        if fileRead != "":
            self.view.showMessage("Arxiu " + filepath)
            self.view.showMessage(fileRead)
        else:
            self.view.showMessage("Arxiu vuit o no s'ha trobat")
    
    def escriureFitxer(self):
        """Appends text if found or creates a file with text that previously was asked to user and displays what happenned
        """
        filepath = self.view.showInputDialog("Nom del arxiu per escriure: ")
        text: str = self.view.showInputDialog("Quin missatge vols posar?: ")
        done = self.model.writeFile(filepath, text)
        if done == False:
            self.view.showMessage("No s'ha pogut fer l'operació")
        else:
            self.view.showMessage("Arxiu " + filepath)
            self.view.showMessage(self.model.readFile(filepath))
    
    def esborrarFitxer(self):
        """Removes a file on the path relative to __main__.py and shows to user if It was done
        """
        filepath = self.view.showInputDialog("Nom del arxiu per esborrar: ")
        if self.model.removeFile(filepath):
            self.view.showMessage("L'arxiu " + filepath + " s'ha esborrat correctament")
        else:
            self.view.showMessage("L'arxiu " + filepath + " no s'ha esborrat")