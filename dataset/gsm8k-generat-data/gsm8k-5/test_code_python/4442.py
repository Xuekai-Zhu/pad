def solution():
    initial_weight = 60  # Thomas' weight vest weighs 60 pounds initially
    percent_increase = 0.6  # Thomas wants to increase the weight by 60%
    new_weight = initial_weight + (percent_increase * initial_weight)  # Thomas' new weight after the increase
    ingot_weight = 2  # Each steel ingot weighs 2 pounds
    num_ingots = new_weight / ingot_weight  # Number of ingots needed to reach the new weight
    ingot_cost = 5  # Each ingot costs $5
    if num_ingots > 10:
        discount = 0.2  # If more than 10 ingots are bought, a 20% discount is given
        total_cost = (num_ingots * ingot_cost) * (1 - discount)  # Total cost with discount
    else:
        total_cost = num_ingots * ingot_cost  # Total cost without discount
    result = total_cost
    return result

print(solution())