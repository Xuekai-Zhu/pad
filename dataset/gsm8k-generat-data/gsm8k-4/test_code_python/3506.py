def solution():
    """Rosie pays for a $.44 piece of candy with a $1 bill. If the cashier gives her the smallest number of coins possible as change, how many coins will Rosie get as change?"""
    # Define the value of the candy and the amount paid
    candy_value = 0.44
    paid_amount = 1.00

    # Calculate the change
    change = paid_amount - candy_value

    # Initialize the coin counters
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    # Calculate the number of each coin needed for the change
    while change > 0:
        if change >= 0.25:
            quarters += 1
            change -= 0.25
        elif change >= 0.10:
            dimes += 1
            change -= 0.10
        elif change >= 0.05:
            nickels += 1
            change -= 0.05
        else:
            pennies += 1
            change -= 0.01
            
    # Calculate the total number of coins
    total_coins = quarters + dimes + nickels + pennies

    result = total_coins
    return result

print(solution())