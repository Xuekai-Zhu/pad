def solution():
    """Tyrone empties his piggy bank and finds two $1 bills, a $5 bill, 13 quarters, 20 dimes, 8 nickels, and 35 pennies. How much money does Tyrone have?"""
    # Define the value of each coin and bill in cents
    ONE_DOLLAR = 100
    FIVE_DOLLARS = 500
    QUARTER = 25
    DIME = 10
    NICKEL = 5
    PENNY = 1

    # Calculate the total value of the bills
    total_bills = (2 * ONE_DOLLAR) + FIVE_DOLLARS

    # Calculate the total value of the coins
    total_coins = (13 * QUARTER) + (20 * DIME) + (8 * NICKEL) + (35 * PENNY)

    # Calculate the total value of all the money
    total_money = total_bills + total_coins

    # Convert the total money to dollars and cents format
    dollars = total_money // 100
    cents = total_money % 100

    # Display the total money
    result = "${}.{}".format(dollars, cents)
    return result

print(solution())