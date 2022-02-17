#4-11 My Pizzas, Your Pizzas

mypizzas = ['peperoni', 'italian', 'beef']
friend_pizzas = mypizzas[:]

friend_pizzas.append('grande')

for pizzas in mypizzas:
	print(f"Masarap para sakin ang {pizzas}.\n")

print(f"Ang tatlong pizza na nabanggit ay masarap para sa akin.\n")

for pizza in friend_pizzas:
	print(f"Paborito ng tropa ko ang {pizza}\n") 