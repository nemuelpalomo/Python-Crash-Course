#3-6 More Guests


guests = ['nemuel', 'rico', 'orgado']

going = []

not_going = []

dinnertable = []

print(f"{guests[0].title()} is going for the dinner tonight.")

print(f"{guests[1].title()} is also going for the dinner tonight.")

print(f"{guests[2].title()} is not going for the dinner tonight.")

going.append(guests[0])
going.append(guests[1])
not_going.append(guests[2])


dinnertable.append(guests[0])
dinnertable.append(guests[1])


print(f"These 2 people are going {going[0].title()} and {going[1].title()}.")
print(f"The dinner table has been occupied by 2 people now.")

uninvited_guests = ['jana', 'alex', 'therese']

party_crashers = []

party_crashers.append(uninvited_guests[0])
party_crashers.append(uninvited_guests[1])
party_crashers.append(uninvited_guests[2])

dinnertable.append(party_crashers[0])
dinnertable.append(party_crashers[1])
dinnertable.append(party_crashers[2])

print(f"The dinner table now occupies more people. {dinnertable}")

print(f"\nHowever. The dinner table can only occupy 3 people, the excess guest must go.")

dinnertable.remove('jana')
dinnertable.remove('therese')

print(f"The dinner table now only has 3 people on it, the two excess uninvited guests were kicked \n\n{dinnertable}\n")

