preis_erwachsene = 5.0
preis_jugendlich = 3.5
preis_kinder = 2.5
preis_premium = 3.0
preis_basis = 4.0

print('### Tarifauskunftsrechener Museum XXX ###')
print('Hallo, geben Sie bitte Ihr Alter ein.')
alter_gast = int(input())

if alter_gast < 14:
    print('### Eintritt Kinder ### ')
    print('Preis: ', preis_kinder, ' Euro ')
elif alter_gast < 18: 
    print('### Eintritt Jugendliche ###')
    print('Preis: ', preis_jugendlich, ' Euro ')
else:
    print('Sind sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ')
    print('Wenn Sie Premium-Mitglied sind, geben Sie "p" ein.')
    print('Wenn Sie Basis-Mitglied seid, geben sie "b" ein.')
    print('Wenn Sie Kein Mitglied sind, drücken Sie eine beliebige andere Taste.')
    antwort_rabatt = input()
    if antwort_rabatt == "p":
        print('### Eintritt Premium-Mitglied ###')
        print('Preis: ', preis_premium, ' Euro ')
    elif antwort_rabatt =="b":
        print('### Eintritt Basis-Mitglied ###')
        print('Preis: ', preis_basis, ' Euro ')
    else:
        print('### Eintritt Erwachsene (voller Preis) ###')
        print('Preis: ', preis_erwachsene,' Euro ')
    
print('Drücken sie eine beliebige Taste um das Programm zu beenden!')
input()
