from proven.comprescistella.model.CCProducte import CCProducte

class CCCistella:
    
    def __init__(self):
        self.listProducte = list()
        self.unity = None
        self.totalPrice = 0.0
    
    def addProdcute(self, CCProducte: CCProducte):
        """Adds a product

        Args:
            CCProducte (CCProducte): CCProduct given to add
        """
        self.listProducte.append(CCProducte)
    
    def recalculateTotalPrice(self):
        """Recalculates the total price 
        """
        self.totalPrice = 0.0
        for producte in self.listProducte:
            self.totalPrice += producte.price
    
    def __eq__(self, other):
        if not isinstance(other, CCCistella):
            return False

        if len(self.listProducte) != len(other.listProducte):
            return False

        for i, producte in enumerate(self.listProducte):
            if producte != other.listProducte[i]:
                return False

        return True
        
    def __hash__(self):
        return hash(tuple(producte.idP for producte in self.listProducte))
    
    def __str__(self) -> str:
        formatted_string = ""
        for producte in self.listProducte:
            formatted_string += producte.mostraProducteSenseStock() + "\n"
        self.recalculateTotalPrice()
        formatted_string += "--------------------------------------------------" + "\n"
        formatted_string += "Total Price: " + str(self.totalPrice) + "\n"
        return formatted_string
    
    def getFactura(self) -> str:
        """Generates a string of a Bill

        Returns:
            str: Formatted string with all the products to print in a Bill
        """
        formatted_string = "----===FACTURA COMPRA CISTELLA===----\n"
        for producte in self.listProducte:
            formatted_string += producte.mostraProducteSenseStock() + "\n"
        formatted_string += "Total: " + str(self.totalPrice) + "\n"
        return formatted_string
    
    def emptyCistella(self):
        self.listProducte.clear()
    