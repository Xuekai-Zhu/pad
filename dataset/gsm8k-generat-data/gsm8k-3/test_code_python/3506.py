def solution():
    """Rosie pays for a $.44 piece of candy with a $1 bill. If the cashier gives her the smallest number of coins possible as change, how many coins will Rosie get as change?"""
    # Define the value of each coin
    PENNY = 0.01
    NICKEL = 0.05
    DIME = 0.10
    QUARTER = 0.25

    # Calculate the amount of change Rosie should receive
    change = 1 - 0.44

    # Calculate the number of quarters in the change
    quarters = int(change // QUARTER)
    change -= quarters * QUARTER

    # Calculate the number of dimes in the change
    dimes = int(change // DIME)
    change -= dimes * DIME

    # Calculate the number of nickels in the change
    nickels = int(change // NICKEL)
    change -= nickels * NICKEL

    # Calculate the number of pennies in the change
    pennies = int(round(change / PENNY))

    # Calculate the total number of coins Rosie will receive as change
    total_coins = quarters + dimes + nickels + pennies

    # Display the total number of coins Rosie will receive
    result = total_coins
    return result

print(solution())