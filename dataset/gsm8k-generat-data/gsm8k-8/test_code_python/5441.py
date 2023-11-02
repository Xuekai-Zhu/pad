def solution():
    # Define the cost of the TV and the difference in cost between the fridge and computer
    tv_cost = 600
    fridge_computer_diff = 500
    
    # Calculate the total cost of the fridge and computer together
    fridge_cost = tv_cost + fridge_computer_diff
    fridge_computer_total = tv_cost + fridge_cost
    
    # Calculate the cost of the computer
    computer_cost = (1600 - fridge_computer_total) / 2
    result = computer_cost
    return result

print(solution())