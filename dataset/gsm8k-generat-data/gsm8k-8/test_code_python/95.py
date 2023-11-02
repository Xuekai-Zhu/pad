def solution():
    # Define the value of each coin in cents
    quarter_value = 25
    nickel_value = 5

    # Calculate the total value of Alice's quarters in cents
    total_quarter_value = 20 * quarter_value

    # Calculate the total number of nickels she receives in exchange for her quarters
    total_nickels = total_quarter_value // nickel_value

    # Calculate the number of iron nickels
    iron_nickels = total_nickels * 0.2

    # Calculate the total value of Alice's money, including the iron nickels
    total_value = total_quarter_value + ((total_nickels - iron_nickels) * nickel_value) + (iron_nickels * 300)

    # Convert the total value back to dollars
    total_value /= 100

    result = total_value
    return result

print(solution())