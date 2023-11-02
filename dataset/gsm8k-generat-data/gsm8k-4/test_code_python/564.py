def solution():
    """Rodney has 35 dollars more than Ian. Ian has half as much money as Jessica has. If Jessica has 100 dollars, how much more money does Jessica have than Rodney?"""
    # Define the initial amount of money Jessica has
    jessica_money = 100

    # Calculate the amount of money Ian has
    ian_money = jessica_money / 2

    # Calculate the amount of money Rodney has
    rodney_money = ian_money + 35

    # Calculate the difference between Jessica's and Rodney's money
    difference = jessica_money - rodney_money

    # Return the result
    result = difference
    return result

print(solution())