def solution():
    
    box1_price_per_contact = 25 / 50
    box2_price_per_contact = 33 / 99

    if box1_price_per_contact < box2_price_per_contact:
        price_per_contact = box1_price_per_contact
    else:
        price_per_contact = box2_price_per_contact

    contacts_per_dollar = 1 / price_per_contact
    result = contacts_per_dollar
    return result

print(solution())