def solution():
    # Define the cost of last year's costume and the percentage increase
    last_year_cost = 250
    percentage_increase = 0.4

    # Calculate the total cost of this year's costume
    total_cost = last_year_cost * (1 + percentage_increase)

    # Calculate the deposit and the amount Jeff had to pay when picking up the costume
    deposit = 0.1 * total_cost
    amount_picked_up = total_cost - deposit

    result = amount_picked_up
    return result

print(solution())