# # Iss text ko question3.txt ke naam ki file mein save karo.
# # Code Example
# rishabh - meerut
# imtiyaz - delhi
# nilima - cochin
# rati - shimla
# ayishah - delhi
# raghu - shimla
# naseer - kanpur
# karthikeyan - delhi
# salma - jaipur
# pankaj - delhi
# brijesh - delhi
# govind - delhi
# puneet - shimla
# siddhi - delhi
# suman - jaipur
# rajeev - shimla
# mohinder - delhi
# rajendra - jaipur
# priyanka - shimla
# neela - delhi
# sashi - jaipur
# sarika - delhi
# deepti - shimla
# harshad - delhi
# trishna - raipur
# pradeep - jaipur
# sekhar - delhi
# nand - delhi
# anoop - delhi
# balwinder - tokyo

# Iss file mein dhyaan se dekhoge toh ek insaan ka naam aur ek sheher ka naam milegaYeh sheher woh sheher hai jisme woh insaaan rehta hai. Ab aapne ek aisa code likhna hai jo:

# 1

# Delhi mein rehne waale logon ko ek alag file mein daale. Delhi waali file ka naam "delhi.txt" hona chaiye.

# 2

# Shimla mein rehne waale logon ko ek alag file mein daale. Shimla waali file na naam "shimla.txt" hona chaiye

# 3

# Aur saare log jo delhi aur shimla mein nahi rehte, unko ek alag file mein daale. Iss file ka naam "others.txt" hona chaiye

# Aapko aisa code likhna hai, jo aisi file mein kitni bhi lines pe chal paye.


# Iss file mein dhyaan se dekhoge toh ek insaan ka naam aur ek sheher ka naam milegaYeh sheher woh sheher hai jisme woh insaaan rehta hai. Ab aapne ek aisa code likhna hai jo:

# 1

# Delhi mein rehne waale logon ko ek alag file mein daale. Delhi waali file ka naam "delhi.txt" hona chaiye.

# 2

# Shimla mein rehne waale logon ko ek alag file mein daale. Shimla waali file na naam "shimla.txt" hona chaiye

# 3

# Aur saare log jo delhi aur shimla mein nahi rehte, unko ek alag file mei, daale. Iss file ka naam "others.txt" hona chaiye

# Aapko aisa code likhna hai, jo aisi file mein kitni bhi lines pe chal paye.

 
# # file=open("exercise.txt","x")
file=open("exercise.txt","w")
file.write("rishabh - meerut\nimtiyaz - delhi\nnilima - cochin\nrati - shimla\nayishah - delh\nraghu - shimla\nnaseer - kanpurkrthkeyan - delhi\nsalma - jaipur\npankaj - delhi\nbrijesh - delhi\ngovind - delhi\npuneet - shimla\n")
file.close()
file=open("exercise.txt","r")
file_data=file.read()
print(file_data)
file.close()










# a=open("meraki q4.txt","r")
# b=a.readline()
# pro=int(b)
# i=0
# while i <len(b):
#     if "delhi" not in b[i] and "shimala" not in b[i]:
#         o=open("other.txt","a")
#         o.write(b[i])
#     if "delhi" in b[i]:
#         d=open("delhi.txt","a")
#         d.write(b[i])
#         d.close()
#     if "shimala" in b[i]:
#         s=open("shimala.txt","a")
#         s.write(b[i])
#         s.close()
#     i+=1
 