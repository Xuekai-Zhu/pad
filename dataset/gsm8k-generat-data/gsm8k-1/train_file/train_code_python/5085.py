def solution():
    """Trip wanted to watch the new action movie in theaters. An evening ticket cost $10 and a large popcorn & drink combo would cost him an additional $10. He noticed on their website, they had a special offer. From 12 noon to 3 pm, save 20% off tickets and 50% off any food combos. How much money could Trip save by going to the earlier movie?"""
    
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