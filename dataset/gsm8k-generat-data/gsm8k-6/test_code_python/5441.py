def solution():
    # Find the total cost of the TV, fridge, and computer
    total_cost = 1600
    tv_cost = 600
    fridge_cost = total_cost - tv_cost
    computer_cost = (fridge_cost - 500) / 2  # fridge costs $500 more than the computer

    result = computer_cost
    return result

print(solution())