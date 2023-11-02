def solution():
    """Faith went to a baking shop and bought flour that cost $5 and a cake stand that costs $28. She then gave the cashier two $20 bills and $3 in loose coins. How much change will she receive?"""
    # Define the cost of the flour and cake stand
    flour_cost = 5
    stand_cost = 28

    # Calculate the total cost of the purchase
    total_cost = flour_cost + stand_cost

    # Calculate the total amount Faith gave to the cashier
    total_paid = 2*20 + 3

    # Calculate the change Faith will receive
    change = total_paid - total_cost

    # return the result
    result = change
    return result

print(solution())