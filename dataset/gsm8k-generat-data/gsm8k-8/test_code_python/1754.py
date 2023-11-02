def solution():
    # Define the initial amount of money
    initial_amount = 2000

    # Define the cost of the furniture
    furniture_cost = 400

    # Calculate the remaining amount of money
    remaining_money = initial_amount - furniture_cost

    # Calculate the amount given to Anna
    anna_share = (3/4) * remaining_money

    # Calculate the amount left with Emma
    emma_remaining = remaining_money - anna_share
    result = emma_remaining
    return result

print(solution())