def solution():
    dimes = pennies + 10
    nickels = dimes * 2
    quarters = 4
    pennies = quarters * 10

    # Calculate the total value of all coins
    total_value = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25)

    # Calculate the number of nickels
    num_nickels = int((total_value - (pennies * 0.01) - (dimes * 0.1) - (quarters * 0.25)) / 0.05)

    result = num_nickels
    return result

print(solution())