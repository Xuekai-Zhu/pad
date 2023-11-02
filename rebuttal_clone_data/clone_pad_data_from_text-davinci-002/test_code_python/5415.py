def solution():
    contacts_1 = 50
    contacts_2 = 99
    price_1 = 25
    price_2 = 33
    contacts_per_dollar_1 = contacts_1 / price_1
    contacts_per_dollar_2 = contacts_2 / price_2
    
    if contacts_per_dollar_1 < contacts_per_dollar_2:
        result = contacts_1
    else:
        result = contacts_2
    return result

print(solution())