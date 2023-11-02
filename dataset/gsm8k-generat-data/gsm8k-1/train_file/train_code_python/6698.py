def solution():
    """Bob has to hire someone to fix his garden. A storm destroyed all 20 of his rose bushes. He decides to replant all the rose bushes. Each rose bush costs $150. He also needs to pay a gardener $30 an hour, 5 hours each day for 4 days. The final expense is 100 cubic feet of soil sold for $5 per cubic foot. How much did the entire gardening project cost?"""
    num_rose_bushes = 20
    cost_per_bush = 150
    total_bush_cost = num_rose_bushes * cost_per_bush
    
    hours_per_day = 5
    num_days = 4
    hourly_rate = 30
    total_gardener_cost = hours_per_day * num_days * hourly_rate
    
    cubic_feet_of_soil = 100
    cost_per_cubic_foot = 5
    total_soil_cost = cubic_feet_of_soil * cost_per_cubic_foot
    
    total_cost = total_bush_cost + total_gardener_cost + total_soil_cost
    
    result = total_cost
    return result

print(solution())