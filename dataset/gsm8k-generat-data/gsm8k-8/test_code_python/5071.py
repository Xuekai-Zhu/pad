def solution():
    # Define the initial balance
    balance = 100

    # Sell two players for $10 million each
    balance += 2 * 10

    # Buy four players for $15 million each
    balance -= 4 * 15

    # Convert the balance to millions of dollars
    balance_in_millions = balance / 1e6

    # Round the result to two decimal places
    result = round(balance_in_millions, 2)
    return result

print(solution())