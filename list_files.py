import os

print(f"The files and folders in {os.getcwd()} are: ")
items = os.listdir('.')
for item in items:
    print(item)
