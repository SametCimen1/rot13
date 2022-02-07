alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrpt(str):
   newStr = ""
   #samet -> s (19 + 26) = 44 % 13 => 5 
   for i in range(len(str)):
       normalIndex = alphabet.index(str[i]) //26 
       newIndex = (normalIndex + 13) % 25
       newStr += alphabet[newIndex]
   return newStr
     
    

encrpted = encrpt("samet")
print(encrpted)
