mexican_pesos = float(input('How many money do you have? '))

dollar_value = 21.21
dollars = mexican_pesos / dollar_value
dollars = round(dollars, 2)
dollars = str(dollars)

print('Do you have $' + dollars + ' dollars')