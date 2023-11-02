def solution():
    # Calculate the total pay Jake wants to earn for the two tasks
    total_pay = 20 * 3  # 1 hour of mowing + 2 hours of planting flowers
    
    # Calculate the pay Jake will receive for mowing the lawn
    lawn_pay = 15

    # Calculate the pay Jake should charge for planting the flowers
    flower_charge = total_pay - lawn_pay
    
    result = flower_charge
    return result

print(solution())