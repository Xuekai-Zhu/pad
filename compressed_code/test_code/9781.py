def solution():
    
    
    evening_ticket_price = 10
    combo_price = 10
    discount_percent = 20
    food_discount_percent = 50
    
    noon_ticket_price = evening_ticket_price - (evening_ticket_price * (discount_percent/100))
    noon_combo_price = combo_price - (combo_price * (food_discount_percent/100))
    total_noon_cost = noon_ticket_price + noon_combo_price
    total_evening_cost = evening_ticket_price + combo_price
    
    savings = total_evening_cost - total_noon_cost
    
    result = savings
    return result

print(solution())