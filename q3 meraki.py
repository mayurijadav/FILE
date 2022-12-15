# Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki file mein nayi line mein daalo. Aapki list yeh rahi:
# Code Example

banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
for i in banks_list:
    a=open("file-question3.tx","w")
    a.write("kotak""\n""HDFC""\n""RBL""\n""SBI""\n""Bank of baroda")
    print(a)









# # second method 
# file=open("bank_name.txt")
# banks_list==["kotak","HDFC","RBL","SBI","BANK OF BARODA"]
# for i in banks_list:
#     print(i)
