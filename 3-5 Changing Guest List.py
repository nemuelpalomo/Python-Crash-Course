# 3-5 Changing Guest List

guests = ['rico', 'nemuel', 'palomo']

print(f"{guests[0].title()} you are invited to a dinner later.")

print(f"{guests[1].title()}, we are inviting you to a dinner for tonight.")

print(f"{guests[2].title()} is invited to a dinner later.")


cant_go = guests.pop(2).title()

print(f"{cant_go} will not be going tonight.")

print(f"However, {guests[0].title()} and {guests[1].title()} are sure to come tonight.")