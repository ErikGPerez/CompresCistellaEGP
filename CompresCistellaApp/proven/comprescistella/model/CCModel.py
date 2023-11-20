import os
from proven.comprescistella.model.CCProducte import CCProducte

class CCModel: #TODO: Complete the model
    
    def __init__(self):
        self.listProducts = list()
    
    def showProducts(self):          
        return self.listProducts
    
    def showBasket(self):
        cosa = CCProducte(342, "Platano", "Fruta", 2.3, 26)
        print(cosa.mostraProducte())
    
    def addBasket(self):
        pass
        
    def loadProducts(self):
        script_dir = os.path.dirname(__file__)
        fileRead = open(script_dir + "/data/products.txt", "r").read()
        listProductsText = fileRead.strip().split(":")
        for productText in listProductsText:
            product = productText.strip().split(",")
            finalProduct = CCProducte(None, None, None, None, None)
            productId = product[0].strip()
            finalProduct.idP = int(productId)
            finalProduct.name = product[1]
            finalProduct.category = product[2]
            finalProduct.price = float(product[3])
            finalProduct.stock = float(product[4])
            print(finalProduct.mostraProducte())
            self.listProducts.append(finalProduct)
                     
               
            
    
    ##################### USER METHODS #####################
    
    def registerFileUser(self, user, password) -> bool:
        """Creates a file with the filepath str given

        Args:
            filepath (str): Text of the filepath to create a file

        Returns:
            bool: True if added, otherwise False
        """
        script_dir = os.path.dirname(__file__)
        try:
            fileWrite = open(script_dir + "/data/uspass.txt", "a")
            fileWrite.write("::" + user + "::" + password)
            return True
        except:
            return False
    
    def readFileUser(self) -> str:
        """Reads the uspass.txt file that contains a list of users and passwords

        Returns:
            str: Returns the text obtained with the read() option
        """
        try:
            script_dir = os.path.dirname(__file__)
            fileRead = open(script_dir + "/data/uspass.txt", "r").read()  
        except:
            return "File not found"
            
        return fileRead
    
    def checkUser(self, user, password, uspass) -> bool:
        """Checks if the user and password is in the list is in the list

        Args:
            user (_type_): _description_
            password (_type_): _description_
            uspass (_type_): _description_

        Returns:
            _type_: _description_
        """
        uspassList = uspass.strip().split("::")
        if user in uspassList and password in uspassList:
            return True
        else:
            return False
    
    
    ####################################################