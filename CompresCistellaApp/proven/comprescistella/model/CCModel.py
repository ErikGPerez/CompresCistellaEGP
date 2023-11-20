import os
from proven.comprescistella.model.CCProducte import CCProducte
from proven.comprescistella.model.CCCistella import CCCistella

class CCModel:
    
    def __init__(self):
        self.listProducts = list()
        self.cistella = CCCistella()
    
    def showProducts(self):
        """Shows the products
        """          
        return self.listProducts
    
    def showBasket(self):
        """Shows the basket

        Returns:
            str: String of the product list
        """
        return self.cistella
    
    def addBasket(self, producte):
        """Adds a Product on a basket

        Args:
            producte (CCProducte): Given producte chosen on controller
        """
        self.cistella.addProdcute(producte)
        
    def generateBill(self):
        """Creates a file with the filepath str given

        Args:
            filepath (str): Text of the filepath to create a file

        Returns:
            bool: True if added, otherwise False
        """
        script_dir = os.path.dirname(__file__)
        try:
            fileWrite = open(script_dir + "/data/factura.txt", "w")
            fileWrite.write(self.cistella.getFactura())
            return True
        except:
            return False
        
    def removeCistella(self):
        """removes on the memory the list of cistella
        """
        self.cistella.emptyCistella()
        
    def loadProducts(self):
        """Load the products on the pruducts.txt data
        """
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