def solution():
    """Thomas buys a weight vest. It weighed 60 pounds and worked well for him in the beginning but after a bit of training he decides he wants to increase the weight by 60%. The weights come in 2-pound steel ingots. Each ingot cost $5 and if you buy more than 10 you get a 20% discount. How much does it cost to get the weight he needs?"""
    
    # Initial weight of the vest
    initial_weight = 60
    
    # Increase in weight after training
    increase_percent = 60
    increase_weight = initial_weight * (increase_percent / 100)
    
    # Total weight of the vest after increase
    total_weight = initial_weight + increase_weight
    
    # Weight of each steel ingot
    ingot_weight = 2
    
    # Total number of ingots needed
    num_ingots = total_weight / ingot_weight
    
    # Cost of each ingot
    ingot_cost = 5
    
    # Cost of buying 10 or more ingots
    bulk_discount = 0.2
    
    # Cost of all ingots needed
    if num_ingots >= 10:
        total_cost = (num_ingots * ingot_cost * (1 - bulk_discount))
    else:
        total_cost = num_ingots * ingot_cost
    
    result = total_cost
    return result

print(solution())