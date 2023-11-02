def solution():
    """90 single use contacts come in 1 box and will last Pete 45 days. Each box is $100.00 and currently 10% off. If he buys 2 boxes of contact, how much will each pair of contacts cost?"""
    contacts_per_box = 90
    days_per_box = 45
    price_per_box = 100
    discount_percent = 10
    boxes_bought = 2
    total_contacts = contacts_per_box * boxes_bought
    total_days = days_per_box * boxes_bought
    discounted_price = price_per_box * (1 - discount_percent/100)
    cost_per_contact = discounted_price / total_contacts
    result = cost_per_contact
    
    return result

print(solution())