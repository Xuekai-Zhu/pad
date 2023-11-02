def solution():
    mowing_pay = 15  # Jake earns $15 for mowing the lawn in 1 hour
    total_time = 3  # Mowing the lawn takes 1 hour, planting flowers takes 2 hours
    desired_pay = 20  # Jake wants to earn $20 per hour

    # Calculate the total pay Jake should earn for 3 hours of work
    total_pay = total_time * desired_pay

    # Subtract the pay for mowing the lawn to get the pay for planting flowers
    flower_pay = total_pay - mowing_pay
    result = flower_pay
    return result

print(solution())