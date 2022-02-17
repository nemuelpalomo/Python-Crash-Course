
#2-3

person_name = "Nemuel Rico Palomo"

personal_message = f"Hello {person_name}, Lets learn some python for one hour!"

print(personal_message)

#2-4

person_name_lowercase = person_name.lower()

person_name_uppercase = person_name.upper()

person_name_titlecase = person_name.title()

print(person_name_lowercase)
print(person_name_uppercase)
print(person_name_titlecase)

#2-5 and 2-6

quote = '"nothing happens until something moves."'

author = "albert einstein"

famous_quote = f"{author.title()} once said, {quote.title()}"

print(famous_quote)

#2-7 

name = "\tnemuel\t\n\trico\t\n\tpalomo\t"

print(name)

print(name.lstrip())
print(name.rstrip())
print(name.strip())