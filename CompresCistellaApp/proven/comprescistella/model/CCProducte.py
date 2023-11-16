class CCProducte: #TODO: Complete the Product constructor
    
    def __init__(self, idP: int, name: str, category: str, price, stock):
        self.idP = idP
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
    
    def __eq__(self, __value: object) -> bool:
        pass
    
    def __hash__(self) -> int:
        pass
    
    def __str__(self) -> str:
        return ("{Id: " + str(self.idP) + ", Name: " + str(self.name) + ", Category: " + str(self.category) + ", Price: " + str(self.price) +", Stock: " + str(self.stock)+ "}")
    
    def compraElProducte(self):
        """Sells the product to user
        """
        pass
        