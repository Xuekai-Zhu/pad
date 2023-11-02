def solution():
    # Convert all coins to their respective values in cents
    quarters = 10 * 25
    dimes = 3 * 10
    nickels = 3 * 5
    pennies = 5

    # Calculate the total value in cents
    total_value = quarters + dimes + nickels + pennies

    # Convert the total value back to dollars
    dollars = total_value / 100

    result = dollars
    return result

print(solution())