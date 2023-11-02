def solution():
    quarters = 10
    dimes = 3
    nickels = 4
    pennies = 200

    # Calculate the total amount of money in cents
    total_cents = (quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1)

    # Convert the total amount of money to dollars
    total_dollars = total_cents / 100
    result = total_dollars
    return result

print(solution())