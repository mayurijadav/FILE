# # we use the above syntax for creating file .
# a=open("creatingfile.txt","x")

 

# # if we want to write in the file we use the below syntax
# a=open("creatingfile.txt","w")
# a.write("whatever we write here it will disply in creatingfile.txt ")
# a.close()


# a=open("creatingfile.txt","r")
# p=a.read()
# print(p)

# a=open("creatingfile.txt","a")
# a.write("\n""this is my second line")
# a.close()

 

a=open("creatingfile.txt","r")
b=a.readline()
print(b)


a=open("creatingfile.txt","r")
b=a.readlines()
print(b)