import os
from proven.comprescistella.model.CCProducte import CCProducte

class CCModel: #TODO: Complete the model
    
    def __init__(self):
        pass
    
    
    def prova(self):
        cosa = CCProducte(342, "Dildo", "Juguetes Sexuales", 34, 26.50)
        print(cosa)
    
    ############# OTHER METHODS - CRUD #####################
    
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
    
    def checkUser(self, user, password, uspass):
        """Checks if the user and password is in the list is in the list

        Args:
            user (_type_): _description_
            password (_type_): _description_
            uspass (_type_): _description_

        Returns:
            _type_: _description_
        """
        uspassList = uspass.strip().split("::")
        print(uspassList)
        if user in uspassList and password in uspassList:
            return True
        else:
            return False
    
    def writeFile(self, filepath, text: str):
        """Writes an existing file or creates one if not

        Args:
            filepath (str): Text of the filepath to create a file
            text (str): Given text to add

        Returns:
            bool: True if added, otherwise False
        """
        try:
            fileWrite = open(filepath, "a")
            fileWrite.write(text)
            return True
        except:
            return False
        
    def removeFile(self, filepath) -> bool:
        """Removes a file with the filepath str given

        Args:
            filepath (str): Text of the filepath to create a file

        Returns:
            bool: True if removed, otherwise False
        """
        try:
            os.remove(filepath)
        except:
            return False
        return True