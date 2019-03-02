import tkinter as tk
import supermarket_content as smc
import jsonreader as routing

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.supermarket = smc.supermarket([],[])
        self.supermarket.sm_from_file("supermarket.txt")
        self.shoppinglist = smc. shoppinglist([])
        self.geometry("400x600")
        self.entry = tk.Entry(self)
        self.searchbutton = tk.Button(self, text="Add", command=self.on_button)
        self.getRouteButton = tk.Button(self, text="Find Route", command=self.find_route)
        self.listbox = tk.Listbox(self)
        self.entry.pack()
        self.searchbutton.pack()
        self.listbox.pack()
        self.getRouteButton.pack()
        self.profile = smc.default
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
        print(posset)
        routing.get_path(self.profile,groceryStops=posset,show=1)




app = SampleApp()
app.mainloop()