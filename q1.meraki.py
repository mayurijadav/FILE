# Iss text ko people1-exercise.txt ke naam ki file mein save karo.
# a=open("peoplel-exercise.txt","x")

# Iss text ko people1-exercise.txt ke naam ki file mein save karo.
# a=open("peoplel-exercise.txt","w")
# a.write("imtiyaz - delhi,nilima - cochin,rati - shimla,ayishah - delhi,raghu - shimla,naseer - kanpur,karthikeyan - delhi,salma - jaipur,pankaj - delhi,brijesh - delhi")
# a.close()


# Aapne jo pichle question mein (Question 1) file download kari hai, usko read karke usme number of lines count kar ke print karein.
#  Aapne sirf uss file ki number of lines Count karne ka code likhna hai.
#  Hint: Har \n ke baad nayi line shuru hoti hai. Aap yeh use kar ke nayi line ka ko pehchan sakte ho.
a=open("peoplel-exercise.txt","r")
x=a.read()
print(x)