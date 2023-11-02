def solution():
    deposit_percentage = 0.1  # Jeff has to put in a 10% deposit
    previous_cost = 250  # The previous year's costume cost $250
    increase_percentage = 0.4  # The new costume is 40% more expensive than the previous year's costume

    # Calculate the amount of Jeff's deposit
    deposit_amount = previous_cost * deposit_percentage

    # Calculate the total cost of the new costume
    total_cost = previous_cost + (previous_cost * increase_percentage)

    # Calculate the amount Jeff has to pay when he picks up the costume
    remaining_amount = total_cost - deposit_amount
    result = remaining_amount
    return result

print(solution())