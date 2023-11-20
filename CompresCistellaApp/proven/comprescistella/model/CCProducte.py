class CCProducte: #TODO: Complete the Product constructor
    
    def __init__(self, idP: int, name, category, price, stock):
        self.idP = idP
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, CCProducte):
            return False

        return self.idP == __value.idP

    def __hash__(self) -> int:
        return hash(self.idP)
    
    def __str__(self) -> str:
        return (str(self.idP) + "," + str(self.name) + "," + str(self.category) + "," + str(self.price) +"," + str(self.stock))
    
    def mostraProducte(self) -> str:
        return ("Id: " + str(self.idP) + ", Nom: " + str(self.name) + ", Categoria: " + str(self.category) + ", Preu: " + str(self.price) +", Stock: " + str(self.stock))
    
    def compraElProducte(self):
        """Sells the product to user
        """
        pass
        