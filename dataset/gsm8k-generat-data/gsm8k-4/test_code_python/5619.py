def solution():
    """Jack is counting out his register at the end of his shift in the shop. His till has 2 $100 bills, 1 $50 bill, 5 $20 bills, 3 $10 bills, 7 $5 bills, 27 $1 bills, and a certain amount of change in coins. If he is supposed to leave $300 in notes as well as all the coins in the till and turn the rest in to the main office, how much money will he be handing in?"""
    # Define the value of each bill/coin in dollars
    BILLS = [100, 50, 20, 10, 5, 1]
    COINS = [0.25, 0.1, 0.05, 0.01]

    # Calculate the total value of bills
    total_bills = sum([2 * BILLS[0], 1 * BILLS[1], 5 * BILLS[2], 3 * BILLS[3], 7 * BILLS[4], 27 * BILLS[5]])

    # Calculate the value of coins
    total_coins = sum([x * 0.01 for x in range(1, 101)])

    # Calculate the value of the entire till
    total_till = total_bills + total_coins

    # Calculate the amount of money to leave in the till
    leave = 300

    # Calculate the amount of money to turn in
    turn_in = total_till - leave

    result = turn_in
    return result

print(solution())