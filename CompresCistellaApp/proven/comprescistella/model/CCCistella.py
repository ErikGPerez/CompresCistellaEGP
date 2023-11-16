from proven.comprescistella.model.CCProducte import CCProducte

class CCCistella:
    
    def __init__(self): #TODO
        self.producte: CCProducte
        self.listProducte = list()
        self.unity
        self.totalPrice
    
    def addCCProdcute(self, CCProducte: CCProducte):
        self.listProducte.append(CCProducte)
        
    