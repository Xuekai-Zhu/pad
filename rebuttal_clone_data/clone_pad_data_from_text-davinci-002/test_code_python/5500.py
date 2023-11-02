def solution():
    cost_of_set = 2000
    gift_card_amount = 200
    discount_percent = 15
    final_discounted_price = cost_of_set - (cost_of_set * (discount_percent/100))
    additional_discount_percent = 10
    final_price = final_discounted_price - (final_discounted_price * (additional_discount_percent/100))
    total_savings = cost_of_set - final_price
    result = final_price
    
    return result

print(solution())