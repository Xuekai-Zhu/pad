def solution():
    cost_of_puppy = 20.00
    cost_of_food = 20.00
    cost_of_treats = 2.50 * 2
    cost_of_toys = 15.00
    cost_of_crate = 20.00
    cost_of_bed = 20.00
    cost_of_collar = 15.00
    total_cost = cost_of_puppy + cost_of_food + cost_of_treats + cost_of_toys + cost_of_crate + cost_of_bed + cost_of_collar
    new_customer_discount = 0.20
    total_cost_with_discount = total_cost - (total_cost * new_customer_discount)
    result = total_cost_with_discount
    
    return result

print(solution())