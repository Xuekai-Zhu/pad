def solution():
    
    box1_price = 25
    box1_contacts = 50
    box1_price_per_contact = box1_price / box1_contacts
    
    box2_price = 33
    box2_contacts = 99
    box2_price_per_contact = box2_price / box2_contacts
    
    if box1_price_per_contact < box2_price_per_contact:
        price_per_contact = box1_price_per_contact
        contacts_per_dollar = 1 / price_per_contact
    else:
        price_per_contact = box2_price_per_contact
        contacts_per_dollar = 1 / price_per_contact
    
    result = contacts_per_dollar
    return result

print(solution())