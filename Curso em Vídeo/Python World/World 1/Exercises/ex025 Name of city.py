# Make a code that read the name of city and verify if the name starts from "Santo"


"""
nameOfCity = str(input("What's the name of city? ")).strip().upper()
separateName = nameOfCity.split()


print("This name starts from 'Santo?' true ou false?")
print("SANTO" in separateName[0])
"""

nameOfCity = str(input("What's the name of city? ")).strip().upper()
if nameOfCity[:5] == "SANTO":
    print("This city starts with 'Santo'.")
else:
    print("This city doesn't starts with 'Santo'.")

