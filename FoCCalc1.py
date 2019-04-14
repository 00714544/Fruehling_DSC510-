#Capture user order for fiber optice cable, assignment 510 3.1, Deb Fruehling.
message = "Welcome to Current Cable"
company = input("What is your company's name?\n")
print ("Welcome",company)
FtFoC = float(input("How many feet of cable do you need?\n"))
CstFOC=0.87
#The script below will calculate the length input with the cost of 0.87.
print ("Your total cost will be:")
print (FtFoC*CstFOC)
