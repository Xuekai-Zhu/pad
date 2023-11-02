def solution():
    """Olivia and Nigel are traveling in Asia.  Olivia has $112 and Nigel has $139. If together they buy six one day passes to a tourist attraction for $28 per ticket, how much money do they have left?"""
    # Define the initial amount of money of Olivia and Nigel
    olivia_money = 112
    nigel_money = 139

    # Define the cost of one day pass to the tourist attraction
    pass_cost = 28

    # Calculate the total cost of six one day passes
    total_cost = 6 * pass_cost

    # Calculate the total amount of money they have left
    total_money = olivia_money + nigel_money - total_cost

    # Display the total amount of money they have left
    result = total_money
    return result

print(solution())