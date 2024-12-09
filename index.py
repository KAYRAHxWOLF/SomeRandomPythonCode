# Declared Variables
# Price variables: 
preis_erwachsene = 5.0  # Price for adults
preis_kinder = 2.5      # Price for children
preis_premium = 3.0     # Price for premium members
preis_basis = 4.0       # Price for basic members
preis_jugendliche = 3.5 # Price for teenagers

# Boolean variable for the loop
u_continue = True

# #######################################
# While Loop | If u_continue = True => execute loop
while u_continue:
    # Print input request
    print('### Tarifauskunftsrechner Museum XXX ###')
    print('Hallo, geben Sie bitte Ihr Alter ein.')

    # This input saves the user's age for the following conditions
    alter_gast = int(input())

    # If age is under 15
    if alter_gast < 15:
        print('### Eintritt Kinder ###')
        print('Preis: ', preis_kinder, ' Euro')

    # If age is under 18 but 15 or older
    elif alter_gast < 18:
        print('### Eintritt Jugendliche ###')
        print('Preis: ', preis_jugendliche, ' Euro')

    # If age is 18 or older
    else:
        # Print membership input request
        print('Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich)')
        print('Wenn Sie Premium-Mitglied sind, geben Sie "p" ein.')
        print('Wenn Sie Basis-Mitglied sind, geben Sie "b" ein.')
        print('Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste.')

        # Input for membership
        antwort_rabatt = input()

        # Check if the user entered "p" for premium membership
        # To lower converts capital letters to lowercase to avoid case sensitivity issues
        if antwort_rabatt.lower() == "p":
            print('### Eintritt Premium-Mitglied ###')
            print('Preis: ', preis_premium, ' Euro')

        # Check if the user entered "b" for basic membership
        # elif is short for "else if"
        elif antwort_rabatt.lower() == "b":
            print('### Eintritt Basis-Mitglied ###')
            print('Preis: ', preis_basis, ' Euro')

        # If the user is not a member
        else:
            print('### Eintritt Erwachsene (voller Preis) ###')
            print('Preis: ', preis_erwachsene, ' Euro')

    # Program asks if the user wants to continue
    print('Wollen Sie einen weiteren Tarif abfragen? y / n')

    # User input for this question
    antwort_neutarif = input()

    # Check if user input is "y" (yes)
    if antwort_neutarif.lower() == 'y':
        print('Weiteren Tarif\n\n\n\n\n')
        continue  # Continue the loop

    # If not "y", end the loop
    else:
        break # End the loop

# #######################################
# Print a goodbye message
print('Viel Spaß!\n\n\n')
print('Drücken Sie eine beliebige Taste, um das Programm zu beenden!')

# Input to prevent the program from closing automatically.
# This allows the user to read the goodbye message and exit manually.
input()
