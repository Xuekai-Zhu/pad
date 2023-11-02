def solution():
    """Thomas buys a weight vest. It weighed 60 pounds and worked well for him in the beginning but after a bit of training he decides he wants to increase the weight by 60%. The weights come in 2-pound steel ingots. Each ingot cost $5 and if you buy more than 10 you get a 20% discount. How much does it cost to get the weight he needs?"""
    vest_weight = 60
    increase_percentage = 0.6
    total_weight = vest_weight * (1 + increase_percentage)
    ingot_weight = 2
    ingot_cost = 5
    if total_weight % ingot_weight == 0:
        total_ingots = int(total_weight / ingot_weight)
    else:
        total_ingots = int(total_weight // ingot_weight) + 1
        
    cost = total_ingots * ingot_cost
    if total_ingots > 10:
        discount = cost * 0.2
        cost -= discount
        
    result = cost
    return result

print(solution())