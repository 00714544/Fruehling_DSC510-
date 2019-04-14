#Capture user order for fiber optice cable, assignment 510 3.1, Deb Fruehling.
message = "Welcome to Current Cable"
company = input("What is your company's name?\n")
print ("Welcome",company)
FtFoC = float(input("How many feet of cable do you need?\n"))
#The script below will calculate the length input and cost.
print ("Your total cost will be:")
if FtFoC<10:
    print(FtFoC*0.87)
if FtFoC>9 and FtFoC<20:
    print(FtFoC*0.79)
if FtFoC>19:
    print(FtFoC*0.73)
