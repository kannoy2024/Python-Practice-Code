#CaesarCodeDe
encryption = input ("Enter the encrypted text: ")
for p in encryption:
    if "a" <= p <= "z":
        print(chr(ord("a")+(ord(p)-ord("a") + 3)%26),end='')
    else:
        print(p,end='\n')


#CaesarCodeDe
print("\n")
decrypt = input ("Enter the encrypted text: ")
for p in decrypt:
    if "a" <= p <= "z":
        print(chr(ord("a")+(ord(p)-ord("a") - 3)%26),end='')
    else:
        print(p,end='\n')