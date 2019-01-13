from guizero import *
import RPi.GPIO as GPIO
import SimpleMFRC522


reader = SimpleMFRC522.SimpleMFRC522()

app = App(title="HackKU Card Write", layout="grid", width=450, height=300)
    
def read_tag():
    id, text = reader.read()
    if id:
        values = text.split(",")
        allergies = ""
        if len(values) == 8:
            if values[1] == "1":
                allergies += "Vegetarian, "
            if values[2] == "1":
                allergies += "Vegan, "
            if values[3] == "1":
                allergies += "Halal, "
            if values[4] == "1" :
                allergies += "Pork, "
            if values[5] == "1":
                allergies += "Lactose, "
            if values[6] == "1":
                allergies += "Peanut, "
            if values[7] != "":
                allergies += values[7]
                
            display_text.set("Name: " + values[0] )
            display_text2.set("Allergies: " + allergies)

                
        
def write_tag():
    name = name_field.get()
    vege = str(vegetarian_field.value)
    vegan = str(vegan_field.value)
    halal = str(halal_field.value)
    pork = str(pork_field.value)
    lactose = str(lactose_field.value)
    peanut = str(peanut_field.value)
    other = other_field.get()
    text = name + "," + vege + "," + vegan + "," + halal + "," + pork  + "," + lactose + "," + peanut + "," + other
    reader.write(text)
    name_field.set("")
    if vegan == "1":
        vegan_field.toggle()
    if vege == "1":
        vegetarian_field.toggle()
    if halal == "1":
        halal_field.toggle()
    if pork == "1":
        pork_field.toggle()
    if lactose == "1":
        lactose_field.toggle()
    if peanut == "1":
        peanut_field.toggle()
    other_field.set("")
        
PushButton(app, text="Read the Card", command=read_tag, align="left", grid=[0,0])
name_text = Text(app, text = "Name", align = "right", grid = [0,1])
name_field = TextBox(app, text="", align="left", width=20, grid=[1,1])
vegetarian_field = CheckBox(app, text="Vegetarian", align="left", width=10, grid=[1,2])
vegan_field = CheckBox(app, text="Vegan", align="left", width=10, grid=[1,3])
halal_field = CheckBox(app, text="Halal", align="left", width=10, grid=[1,4])
pork_field = CheckBox(app, text="Pork", align="left", width=10, grid=[1,5])
lactose_field = CheckBox(app, text="Lactose", align="left", width=10, grid=[1,6])
peanut_field = CheckBox(app, text="Peanut", align="left", width=10, grid=[1,7])
other_field = TextBox(app, text="", align="left", width=20, grid=[1,9])

display_text = Text(app, text = "Name:", size=12, font="Courier New", color = "blue", grid= [1,20], align= "left")
display_text2 = Text(app, text = "Allergies: ", size=12, font="Courier New", color = "red", grid= [1,25], align= "left")

PushButton(app, text="Write to Card", command=write_tag, align="left", grid=[1,0])

app.display()
