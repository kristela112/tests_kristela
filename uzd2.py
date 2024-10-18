#Kristela Broka 18. oktobris
#Rakstu kodu, lai jautā ievadīt paroli
#Rakstu kodu ja ir pareiza parole tad piekļuve ir atļauta un pārtrauc cikla darbību
#Rakstu kodu ja ir piekļuve liegta tad pieprasīt lai ievada paroli vēlreiz 

while True:
    entered_password = input ("Lūdzu ievadiet paroli :")
    if entered_password == correct_password:
        print("Piekļuve atļauta!")
        break 
    else:
        print("Piekļuve liegta. Mēģiniet vēlreiz.")
