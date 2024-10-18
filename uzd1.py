#Kristela Broka 18. oktobris
#Rakstu kodu, lai pajautā manu vecumu
#Rakstu kodu lai izprintētu kas es esmu bērns, tīns vai pieaugušais 

vecums = int(intput("Lūdzu ievadiet savu vecumu:"))
if vecums <13:
    print("Tu esi bērns")
elif 13 <= vecums <= 19:
    print("Tu esi tīnis")
else:
    print("Tu esi pieaugušāis")