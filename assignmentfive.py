class Smartphone:
    #class attribute of color black
    color = "black"
    
    #use constructors to initialize each object 
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def browse(self):
        print ("Access the internet")
    
phone1 = Smartphone("samsung", 2025)
print(phone1.model)
print(phone1.year)

#inheritence class iphone from smartphone    
class Iphone(Smartphone):
    #polymorphism function
    def browse(self):
        print("Access google thru the internet")
        
x = Iphone("six", "2012")            
for i in (x, phone1):
    print(x.model)
    print(x.year)
    i.browse()