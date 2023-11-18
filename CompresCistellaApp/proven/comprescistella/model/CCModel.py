import os
from proven.comprescistella.model.CCProducte import CCProducte

class CCModel: #TODO: Complete the model
    
    def __init__(self):
        pass
    
    
    def prova(self):
        cosa = CCProducte(342, "Dildo", "Juguetes Sexuales", 23, 34.50)
        print(cosa)
    
    ############# OTHER METHODS - CRUD #####################
    
    def createFile(self, filepath) -> bool:
        """Creates a file with the filepath str given

        Args:
            filepath (str): Text of the filepath to create a file

        Returns:
            bool: True if added, otherwise False
        """
        cond = False
        
        if open(filepath, "x"):
            cond = True
        return cond
    
    def readFileUser(self) -> str:
        """Reads a file with the filepath str given

        Args:
            filepath (str): Text of the filepath to create a file

        Returns:
            str: Returns the text obtained with the read() option
        """
        try:
            fileRead = open("data/uspass.txt", "r").read()  
        except:
            return "File not found"
            
        return fileRead
    
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