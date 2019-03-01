#Importing csv: to read the content of a supermarket or shopping list from a simple csv file
import csv

#Creating the necessary classes for the contents of the super market, shopping list and items themselves 
class item:
    #Initialisation function of the class
    def __init__(self, name, position, price, category, eco, nutri):
        #Setting the classes variables
        self.name = name                                        #Product-id
        self.pos_id = position                                  #Position of the item in the supermarket
        self.price = float(price)                               #Product price
        self.cat = category                                     #Product category (e.g. Meat, dairy)
        self.eco = eco                                          #Eco-score for the product (TBD)
        self.nutri = nutri                                      #Nutri-score for the product (A,B,C,D,E)
    #Function for printing an item to the terminal (returns a string which can be printed)
    def __repr__(self):
        return "%s" %(self.name)

class supermarket:
    #Initialisation function
    def __init__(self, items, categories):
        self.items = items
        self.cats = categories
    def sm_from_file(self, filename):
        #Opening the file
        with open(filename, 'r') as infile:
            content = list(csv.reader(infile, delimiter = ';'))
            for i in range(1, len(content)):
                l = content[i]
                new_item = item(l[0], l[1], l[2], l[3], l[4], l[5])
                if new_item not in self.items:
                    self.items.append(new_item)
    def update_cats(self):
        for it in self.items:
            if it.cat not in self.cats:
                self.cats.append(it.cat)
    def get_items(self):
        return self.items
    def get_categories(self):
        return self.cats
             
class shoppinglist:
    #Initialisation function
    def __init___(self, items):
        self.items = list(items)
    def categories(self):
        return set([item.cat for item in self.items])           #Returns a set with all the unique categories of the items on the shoppinglist
    def pos_ids(self):
        return set([item.pos_id for item in self.items])        #Returns a set with all the unique position ids for the items on the shoppinglist
    def add_to_list(self, add_item):
        self.items.append(add_item)

#Function: takes input file from csv with all the item variables, and initialising them, along with the supermarket.
def items_sm_from_file(filename, market):
    #Opening the file
    with open(filename, 'r') as infile:
        content = list(csv.reader(infile, delimiter = ';'))
        items = []
        cats = []
        for i in range(1, len(content)):
            vars()[content[i][0]] = item(content[i][0], content[i][1], content[i][2], content[i][3], content[i][4], content[i][4]) #Initialising the item
            #Adding the items and the categories into a list
            print(content[i][0])
            items.append(vars()[content[i][0]])
            cats.append(vars()[content[i][0]].cat)
        #Updating the markets to add the new items and categories
        market.items = market.items.union(set(items))
        market.cats = market.cats.union(set(cats))


market = supermarket([],[])
market.sm_from_file("supermarket.txt")
market.update_cats()
print(market.get_items())
print(market.get_categories())