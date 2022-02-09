alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
def encrpt(str):
   newStr = ""
   #samet -> s (19 + 26) = 44 % 13 => 5 
   for i in range(len(str)):
       currentIndex = 0
       for index,letter in enumerate(alphabet):
           if(letter) == str[i]:
            currentIndex = index
       if str[i] == " ":
            currentIndex  = 26
            newStr += " "
       
       else:
            newIndex = (currentIndex + 13) % 26
            newStr += alphabet[newIndex]
       #18 + 13 -> 31 % 26 -> 5

   return newStr
     
    

encrpted = encrpt("hello i am encrypted")
print(encrpted)
