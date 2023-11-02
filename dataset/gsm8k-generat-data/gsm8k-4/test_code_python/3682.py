def solution():
    """Gail has some bills in her wallet which amount to $100. She has four $5 bills and three $20 bills, and the rest are $10 bills. How many $10 bills are in her wallet?"""
    # Define the total amount of money and the number of $5 and $20 bills
    total_money = 100
    num_fives = 4
    num_twenties = 3

    # Calculate the total value of $5 and $20 bills
    total_fives = num_fives * 5
    total_twenties = num_twenties * 20

    # Calculate the total value of $10 bills
    total_tens = total_money - total_fives - total_twenties

    # Calculate the number of $10 bills
    num_tens = total_tens / 10

    # Return the result
    result = int(num_tens)
    return result

print(solution())