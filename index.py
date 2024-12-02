preis_erwachsene = 5.0
preis_kinder = 2.5
preis_premium = 3.0
preis_basis = 4.00
preis_jugendliche = 3.5
u_continue = True
# #############
while u_continue:
    print('### Tarifauskunftsrechener Museum XXX ###')
    print('Hallo, geben Sie bitte Ihr Alter ein.')
    alter_gast = int(input())
    if alter_gast < 14:
        print('### Eintritt Kinder ### ')
        print('Preis: ', preis_kinder, ' Euro ')
    elif alter_gast < 17:
        print('### Eintritt Jugendliche ### ')
        print('Preis: ', preis_jugendliche,' Euro')  
    else:
        print('Sind sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ')
        print('Wenn Sie Premium-Mitglied sind, geben Sie "p" ein.')
        print('Wenn Sie Basis-Mitglied seid, geben sie "b" ein.')
        print('Wenn Sie Kein Mitglied sind, drücken Sie eine beliebige andere Taste.')
        antwort_rabatt = input()
        if antwort_rabatt.lower() == "p":
            print('### Eintritt Premium-Mitglied ###')
            print('Preis: ', preis_premium, ' Euro ')
        elif antwort_rabatt.lower() =="b":
            print('### Eintritt Basis-Mitglied ###')
            print('Preis: ', preis_basis, ' Euro ')
        else:
            print('### Eintritt Erwachsene (voller Preis) ###')
            print('Preis: ', preis_erwachsene,' Euro ')
    print('Wollen Sie einen weiteren Tarif abfragen? y / n')
    antwort_neutarif = input()
    if antwort_neutarif.lower() == 'y':
        print('Weiteren Tarif\n\n\n\n\n')
        continue
    else:
        break
# #############
print('Viel Spass!\n\n\n')
print('Drücken sie eine beliebige Taste um das Programm zu beenden!')
input()
