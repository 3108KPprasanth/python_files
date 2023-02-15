"""     '''using copyfile() of shutil'''
import shutil
shutil.copyfile("source.txt", "destination.txt")

"""    '''using with and as keyword'''

with open("source.txt","r") as source:
    with open("destination.txt","w") as destination:
        for line in source:
            destination.write(line)

source.close()
destination.close()

