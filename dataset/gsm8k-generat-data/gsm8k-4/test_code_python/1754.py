def solution():
    """Emma got $2000 from the bank. She bought $400 of furniture and gave 3/4 of the rest to her friend Anna. How much is left with Emma?"""
    # Define the initial amount of money Emma received
    initial_money = 2000

    # Define the amount of money Emma spent on furniture
    furniture_cost = 400

    # Calculate the amount of money Emma has left after buying furniture
    money_left = initial_money - furniture_cost

    # Calculate the amount of money Emma gave to her friend Anna
    anna_money = money_left * (3/4)

    # Calculate the amount of money Emma has left
    emma_money = money_left - anna_money

    # Return the amount of money Emma has left
    result = emma_money
    return result

print(solution())