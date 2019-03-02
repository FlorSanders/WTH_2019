import tkinter as tk
import supermarket_content as smc
import jsonreader as routing

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #Initialising the variables
        self.supermarket = smc.supermarket([],[])
        self.supermarket.sm_from_file("supermarket.txt")
        self.shoppinglist = smc.shoppinglist([])
        #Starting the frame
        self.geometry("400x600")
        #Entry, search elements
        self.entryLabel = tk.Label(self, text="Add ingredients:")
        self.entry = tk.Entry(self)
        self.searchbutton = tk.Button(self, text="Add", command=self.on_button)
        self.getRouteButton = tk.Button(self, text="Find Route", command=self.find_route)
        #Field with shopping list
        self.listbox = tk.Listbox(self)
        #Recipe-adding elements
        self.recipeLabel = tk.Label(self, text="Add recipe:")
        self.recipeOptions = ["Spaghetti bolognese", "Cheese burger", "Seasonal"]
        self.recipitem = tk.StringVar(self)
        self.recipitem.set(self.recipeOptions[0])
        self.recipedropdown = tk.OptionMenu(self, self.recipitem, *self.recipeOptions)
        self.recipeButton = tk.Button(self, text="Add", command=self.add_recipe)
        #Reset button
        self.resetButton = tk.Button(self, text="Reset", command=self.reset)
        #Waiting table printer
        self.waitLabel = tk.Label(self, text="Check waiting times:")
        self.waitOptions = list(self.supermarket.table.keys())
        self.waititem = tk.StringVar(self)
        self.waititem.set(self.waitOptions[5])
        self.waitdropdown = tk.OptionMenu(self, self.waititem, *self.waitOptions)
        self.waitButton = tk.Button(self, text="Show", command =self.show_wait)
        #Perfect hour to go printer
        self.timevalue = 0
        self.timeButton = tk.Button(self, text="Give ideal shopping time", command = self.show_time)
        self.timestring = "The ideal time to go shopping is: " + str(self.timevalue)
        self.called = 0
        self.timeLabel = tk.Label(self, text=self.timestring)
        #Configuring application structure
        self.entryLabel.pack()
        self.entry.pack()
        self.resetButton.pack()
        self.searchbutton.pack()
        self.listbox.pack()
        self.getRouteButton.pack()
        self.recipeLabel.pack()
        self.recipedropdown.pack()
        self.recipeButton.pack()
        self.profile = smc.default
        self.waitLabel.pack()
        self.waitdropdown.pack()
        self.waitButton.pack()
        self.timeButton.pack()
        self.timeLabel.pack()
        #image = Image.open('image.png')
        #display = ImageTk.PhotoImage(Image.open(image))
#
 #        = Label(root, image=display)
  #      label.pack()

    def on_button(self):
        searchitem = self.entry.get()
        founditem = self.supermarket.search_item(searchitem)
        if founditem != None:
            self.shoppinglist.add_to_list(founditem)
            self.listbox.insert("end",founditem.name)

    def find_route(self):
        posset = self.shoppinglist.pos_ids()
        routing.get_path(self.profile,groceryStops=posset,show=1, createAnim=1)
    
    def add_recipe(self):
        recipe = self.recipitem.get()
        if recipe == self.recipeOptions[0]:
            recipe = smc.bolognese
        elif recipe == self.recipeOptions[1]:
            recipe = smc.burger
        elif recipe == self.recipeOptions[2]:
            recipe = smc.season
        for item in recipe.items:
            self.shoppinglist.add_to_list(item)
            self.listbox.insert("end",item.name)

    def reset(self):
        self.shoppinglist = smc.shoppinglist([])
        self.listbox.delete(0, 'end')
    
    def show_wait(self):
        day = self.waititem.get()
        self.supermarket.get_waiting_time(day)
    
    def show_time(self):
        day = self.waititem.get()
        self.timevalue = self.supermarket.get_ideal_time(day)
        self.timestring = "The ideal time to go shopping is: " + str(self.timevalue)
        self.timeLabel['text'] = self.timestring


app = SampleApp()
app.mainloop()