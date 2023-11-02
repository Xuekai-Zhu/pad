def solution():
    """Oliver had $9, then he saved $5 from his allowance and spent $4 on a frisbee and $3 on a puzzle. His friend gives him another $8 as it's his birthday. How much money does Oliver have left?"""
    # Initialize Oliver's starting amount
    oliver_money = 9

    # Add the amount he saved from his allowance
    oliver_money += 5

    # Subtract the money spent on the frisbee and puzzle
    oliver_money -= 4
    oliver_money -= 3

    # Add his birthday gift from his friend
    oliver_money += 8

    # Display the amount of money Oliver has left
    result = oliver_money
    return result

print(solution())