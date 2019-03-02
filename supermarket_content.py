#Importing csv: to read the content of a supermarket or shopping list from a simple csv file
import csv
import matplotlib.pyplot as plt
import numpy as np

#Creating the necessary classes for the contents of the super market, shopping list and items themselves 
class item:
    #Initialisation function of the class
    def __init__(self, name, position, category, eco, nutri):
        #Setting the classes variables
        self.name = name                                        #Product-id
        self.pos_id = position                                  #Position of the item in the supermarket
        self.cat = category                                     #Product category (e.g. Meat, dairy)
        self.eco = eco                                          #Eco-score for the product (TBD)
        self.nutri = nutri                                      #Nutri-score for the product (A,B,C,D,E)
    #Function for printing an item to the terminal (returns a string which can be printed)
    def __repr__(self):
        return "%s" %(self.name)

class supermarket:
    #Initialisation function
    def __init__(self, items, categories):
        self.items = items                                      #List of the items available at the supermarket
        self.cats = categories                                  #List of categories in the supermarket
        self.pricelist = {}                                     #Price table for the products in the supermarket
        self.table = {"Monday":  [3,3,4,7,3,2,4,8,10,8,3], "Tuesday":  [4,3,4,7,2,5,4,8,10,8,3], "Wednesday":  [1,3,4,6,3,5,4,8,7,8,3], "Thursday":  [3,3,4,6,3,5,4,5,7,5,2], "Friday":  [2,3,4,1,8,5,4,7,11,9,1], "Saturday":  [1,3,4,5,7,4,4,7,8,5,3], "Sunday":  [2,2,4,5,7,4,3,7,8,4,3]}
    def sm_from_file(self, filename):                           #This function reads needed data for a supermarket in from a csv file
        #Opening the file
        with open(filename, 'r') as infile:
            content = list(csv.reader(infile, delimiter = ';'))
            for i in range(1, len(content)):
                l = content[i]
                new_item = item(l[0], l[1], l[3], l[4], l[5])
                self.pricelist[l[0]] = float(l[2])
                if new_item not in self.items:
                    self.items.append(new_item)
        self.update_cats()
    def update_cats(self):                                      #Updates the categories (needs to happen whenever products are added)
        for it in self.items:
            if it.cat not in self.cats:
                self.cats.append(it.cat)
    def get_items(self):                                        #Returns all items available at the supermarket
        return self.items
    def get_items_sorted(self, sorttype="price", rev=0):        #Returns all items sorted on "cost" "eco" or "nutri", possibly in reversed order (std. "cost", in order)
        if sorttype == "price":
            st = lambda x: self.pricelist[x.name]
        elif sorttype == "eco":
            st = lambda x: x.eco
        elif sorttype == "nutri":
            st = lambda x:x.nutri
        return sorted(self.items, key=st, reverse = rev)
    def get_categories(self):                                   #Returns all the categories from the supermarket
        return self.cats
    def get_pricelist(self):                                    #Gives the supermarket pricelist
        return self.pricelist
    def search_item(self, term):                                #Receives a string which it uses to look for an item in the supermarket
        for item in self.items:
            if item.name == term.lower():
                return item
    def get_waiting_time(self, day):
        objects = range(9, 20)
        y_pos = range(len(objects))
        time = self.table[day]
        plt.figure(90)
        plt.bar(y_pos, time, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Usage')
        plt.title('Programming language usage')
 
        plt.show(90)
    def get_ideal_time(self, day):
        ival = 20
        iarg = 1
        for i in range(len(self.table[day])):
            val = self.table[day][i]
            if val < ival:
                ival = val
                iarg = i + 9
        return iarg
             
class shoppinglist:
    #Initialisation function
    def __init__(self, items):
        self.items = list(items)
    def __repr__(self):                                         #Makes it so the list variable actually can be printed                            
        return "%s" %(self.items)                               
    def categories(self):                                       #Returns a set with all the unique categories of the items on the shoppinglist
        return set([item.cat for item in self.items])           
    def pos_ids(self):                                          #Returns a set with all the unique position ids for the items on the shoppinglist
        return set([int(item.pos_id) for item in self.items])        
    def add_to_list(self, add_item):                            #Adds an item to the shopping list
        self.items.append(add_item)                   
    def rem_from_list(self, rem_item):
        if rem_item in self.items:                              #Checks whether the item is in the shopping list
            self.items.remove(rem_item)                         #And removes it if it is
    def get_total_price(self, market):                          
        price = 0
        pricelist = market.get_pricelist()
        for it in self.items:
            price += pricelist[it.name]
        return price
    def compare_supermarkets(self, markets):                    #Compares supermarkets from a list, returns dictionary with market:price combination
        prices = {}                                             
        for market in markets:
            price = self.get_total_price(market)
            prices[market] = price
        return prices
        
class profile:
    def __init__(self, weights):
        self.weights = weights
    def __repr__(self):
        return "%s" %(self.weights)
    def get_weights(self):
        return self.weights

#Basic character profiles
default = profile([1]*15)
health = profile([1,1,2,0.1,3,3,1,3,3,1.5,0.1,2,0.1,1.5,0.1])
party = profile([1,1,1,3,0.7,0.1,1,0.1,0.7,1,3,1,3,1,3])

#Starting a market to get items from
mt = supermarket([], [])
mt.sm_from_file("supermarket.txt")

#Basic recipe shopping list
bolognese = shoppinglist([mt.search_item("tomato"),mt.search_item("garlic"),mt.search_item("onion"),mt.search_item("pork"),mt.search_item("spaghetti"),mt.search_item("courgette")])
burger = shoppinglist([mt.search_item("burger"), mt.search_item("bread"), mt.search_item("cheese"), mt.search_item("lettuce"), mt.search_item("tomato")])
season = shoppinglist([mt.search_item("sprouts"), mt.search_item("steak"), mt.search_item("potato")])

##################"TESTING AREA"#############################
#market = supermarket([], [])
#market.sm_from_file("supermarket.txt")
#my_item = market.search_item("bread")
#print(my_item.pos_id)