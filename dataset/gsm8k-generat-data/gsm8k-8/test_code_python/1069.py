def solution():
    # Define the value of a dime, quarter, and nickel in cents
    dime_value = 10
    quarter_value = 25
    nickel_value = 5

    # Calculate the total value of the coins Maria had before
    total_value_before = 4 * dime_value + 4 * quarter_value + 7 * nickel_value

    # Calculate the total value of the five quarters her mom gave her
    total_value_now = total_value_before + 5 * quarter_value

    # Convert the total value to dollars and return the result
    result = total_value_now / 100
    return result

print(solution())