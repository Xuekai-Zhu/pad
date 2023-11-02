def solution():
    """Sean buys 3 cans of soda, 2 soups, and 1 sandwich. Each soup cost as much as the 3 combined sodas. The sandwich cost 3 times as much as the soup. If the soda cost $1 how much did everything cost together?"""
    # Define the cost of soda
    soda_cost = 1

    # Calculate the cost of 3 cans of soda
    soda_total_cost = soda_cost * 3

    # Calculate the cost of one soup in terms of soda cost
    soup_cost_in_soda = soda_cost * 3

    # Calculate the cost of 2 soups
    soup_total_cost = soup_cost_in_soda * 2

    # Calculate the cost of the sandwich in terms of soda cost
    sandwich_cost_in_soda = soup_cost_in_soda * 3

    # Calculate the total cost in terms of soda cost
    total_cost_in_soda = soda_total_cost + soup_total_cost + sandwich_cost_in_soda

    # Convert the total cost to dollars
    total_cost_in_dollars = total_cost_in_soda * soda_cost

    # return the result
    result = total_cost_in_dollars
    return result

print(solution())