def solution():
    # Calculate the total value of the coins Maria already had
    total_value = (4 * 0.10) + (4 * 0.25) + (7 * 0.05)  # 4 dimes = 40 cents, 4 quarters = 1 dollar, 7 nickels = 35 cents

    # Add the value of the 5 additional quarters from her mom
    total_value += (5 * 0.25)

    # Convert the total value to dollars
    total_value_dollars = total_value / 100
    result = total_value_dollars
    return result

print(solution())