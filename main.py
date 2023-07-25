import storing
import detecting

print("**** Select Choice ****",end="\n")
print("1. Detecting Face ")
print("2. Storing Images")
val = int(input("Enter your Choice :: "))

#Storing The images
if val == 1:
    obj = detecting.detects()
    obj.detection()
elif val == 2:
    obj = storing.store()
    obj.storee()