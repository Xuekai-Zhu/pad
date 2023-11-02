def solution():
    # Define the initial amount of money
    initial_amount = 20

    # Calculate the amount spent on snacks
    snacks_cost = initial_amount / 5

    # Calculate the remaining amount after buying snacks
    remaining_amount = initial_amount - snacks_cost

    # Calculate the amount spent on necessities
    necessities_cost = 3/4 * remaining_amount

    # Calculate the final amount of money remaining
    remaining_money = remaining_amount - necessities_cost

    result = remaining_money
    return result

print(solution())