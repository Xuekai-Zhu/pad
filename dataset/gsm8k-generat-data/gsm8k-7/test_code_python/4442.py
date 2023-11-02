def solution():
    current_weight = 60
    desired_increase = 0.6
    ingot_weight = 2
    ingot_cost = 5
    discount_threshold = 10
    discount = 0.2
    
    # Calculate the new desired weight
    desired_weight = current_weight * (1 + desired_increase)
    # Calculate the weight difference in pounds
    weight_difference = desired_weight - current_weight

    # Calculate the number of ingots needed
    num_ingots = weight_difference / ingot_weight

    # Calculate the total cost of the ingots
    if num_ingots <= discount_threshold:
        total_cost = num_ingots * ingot_cost
    else:
        discounted_price = ingot_cost * (1 - discount)
        total_cost = (discounted_price * num_ingots) + (ingot_cost * discount_threshold)

    result = total_cost
    return result

print(solution())