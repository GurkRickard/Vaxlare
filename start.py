import os
import vaxla

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t -Växlare- \n")

    pris = input("\tMata in pris på varan i kr: ")
    inbet = input("\tInbetalt belopp i kr: ")

    #Anropar växlingens funktion
    exChangeNow(int(pris), int(inbet))

    #definerar växlings funktion som skriver ut växling
def exChangeNow(priset, inbetalning):
    print("test" + str(priset))


main()