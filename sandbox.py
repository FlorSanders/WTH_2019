#Creating the necessary classes for the contents of the super market, shopping list and items themselves
class item:
    #Initialisation function of the class
    def __init__(self, name, position, price, category, eco, nutri):
        #Setting the classes variables
        self.name = name                                        #Product-id
        self.pos_id = position                                  #Position of the item in the supermarket
        self.price = price                                      #Product price
        self.cat = category                                     #Product category (e.g. Meat, dairy)
        self.eco = eco                                          #Eco-score for the product
        self.nutri = nutri                                      #Nutri-score for the product (A,B,C,D,E)

#Not yet sure if we need this
#class supermarket:
#    #Initialisation function
#    def __init__(self, items, categories):
#        self.items = items
#        self.cats = categories

class shoppinglist:
    #Initialisation function
    def __init___(self, items):
        self.items = items
    def categories(self):
        return set([item.cat for item in self.items])           #Returns a set with all the unique categories of the items on the shoppinglist
    def pos_ids(self):
        return set([item.pos_id for item in self.items])        #Returns a set with all the unique position ids for the items on the shoppinglist