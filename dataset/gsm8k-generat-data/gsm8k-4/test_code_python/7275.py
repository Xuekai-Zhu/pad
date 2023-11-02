def solution():
    """John goes to the store to buy Slurpees and gives them $20. Slurpees cost $2 each and he got $8 in change. How many Slurpees did he buy?"""
    # Define the total amount of money John gave to the store
    total_money = 20

    # Define the amount of money John got back in change
    change = 8

    # Calculate the amount of money John spent on Slurpees
    slurpee_cost = total_money - change

    # Calculate the number of Slurpees John bought
    slurpee_count = slurpee_cost / 2

    result = slurpee_count
    return result

print(solution())