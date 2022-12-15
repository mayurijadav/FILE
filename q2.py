# # f=open("demofile.txt","x")

# f=open("demofile.txt","w")
# f.write("mayuri dhiraj kadam")
# f.close()

# m=open("mayu.txt","x")

# a=open("people.txt","w")
# a.write("mayuri dhiraj kadam")
# a.close()

a=open("people.txt","r")
b=a.readline()
pro=int(b)
i=0
while i <len(b):
    if "delhi" not in b[i] and "shimala" not in b[i]:
        o=open("other.txt","a")
        o.write(b[i])
    if "delhi" in b[i]:
        d=open("delhi.txt","a")
        d.write(b[i])
        d.close()
    if "shimala" in b[i]:
        s=open("shimala.txt","a")
        s.write(b[i])
        s.close()
    i+=1