name = "Shashindu Chamika"

print(name)
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize()) # Only captialize the first letter of the first word

print()

# find() and index()
print(name.find("S"))
print(name.find("z"))
print(name.find("a", 10))
print(name.rfind("a"))

print(name.index("S"))
# print(name.index("Z")) # Show an error for this - Main difference with find method

# alignment
print(name.center(50,"-"))
print(name.ljust(20,"-"))
print(name.rjust(20))

# strip 
name2 = "--Nisansal Priyangani"
print(name2)
print(name2.strip('-'))
print(name2.lstrip())
print(name2.rstrip())