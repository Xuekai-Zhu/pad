def solution():
    """Jack is counting out his register at the end of his shift in the shop. His till has 2 $100 bills, 1 $50 bill, 5 $20 bills, 3 $10 bills, 7 $5 bills, 27 $1 bills, and a certain amount of change in coins. If he is supposed to leave $300 in notes as well as all the coins in the till and turn the rest in to the main office, how much money will he be handing in?"""
    # Define the value of each type of bill and coin
    HUNDRED = 100
    FIFTY = 50
    TWENTY = 20
    TEN = 10
    FIVE = 5
    ONE = 1

    # Calculate the total value of bills
    total_bills = 2*HUNDRED + 1*FIFTY + 5*TWENTY + 3*TEN + 7*FIVE + 27*ONE

    # Calculate the value of coins
    coin_value = 0 # initialize coin value
    # Add value of each type of coin
    coin_value += 25 * 4 # 4 quarters
    coin_value += 10 * 3 # 3 dimes
    coin_value += 5 * 2 # 2 nickels
    coin_value += 1 * 4 # 4 pennies

    # Calculate the total value of the register
    total_value = total_bills + coin_value

    # Calculate the amount Jack is supposed to leave
    leave = 300

    # Calculate the amount Jack is handing in
    hand_in = total_value - leave

    # Display the amount Jack is handing in
    result = hand_in
    return result

print(solution())