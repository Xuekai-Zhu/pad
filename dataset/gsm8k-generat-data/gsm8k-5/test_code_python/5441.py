def solution():
    total_budget = 1600  # total budget is $1600
    tv_cost = 600  # cost of the TV is $600
    fridge_cost = tv_cost + 500  # cost of the fridge is $500 more than the computer

    # Calculate how much money is left for the computer after buying the TV and fridge
    remaining_budget = total_budget - tv_cost - fridge_cost

    # Calculate the cost of the computer
    computer_cost = remaining_budget
    result = computer_cost
    return result

print(solution())