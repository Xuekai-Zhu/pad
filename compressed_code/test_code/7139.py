def solution():
    
    adult_ticket_price = 30
    child_ticket_price = adult_ticket_price / 2
    num_adults = 10 - 4  
    num_children = 4
    total_price = (adult_ticket_price * num_adults) + (child_ticket_price * num_children)
    discount = total_price * 0.2 if num_adults + num_children >= 6 else 0
    total_price_with_discount = total_price - discount + 5  
    result = total_price_with_discount
    return result

print(solution())