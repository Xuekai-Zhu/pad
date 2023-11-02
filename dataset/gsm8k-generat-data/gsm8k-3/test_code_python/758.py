def solution():
    """Faith went to a baking shop and bought flour that cost $5 and a cake stand that costs $28. She then gave the cashier two $20 bills and $3 in loose coins. How much change will she receive?"""
    # Calculate the total cost of the items bought
    total_cost = 5 + 28

    # Calculate the total amount of money given by Faith
    total_paid = 20 * 2 + 3

    # Calculate the change to give back to Faith
    change = total_paid - total_cost

    # Display the change
    result = change
    return result

print(solution())