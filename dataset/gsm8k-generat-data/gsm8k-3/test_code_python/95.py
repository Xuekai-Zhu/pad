def solution():
    """Alice has 20 quarters. She wants to exchange them for nickels and so she goes to the bank. After getting back from the bank, she discovers that 20% of the nickels are iron nickels worth $3 each. What is the total value of her money now?"""
    # Define the initial value of the quarters and the exchange rate
    quarters_value = 20 * 0.25
    exchange_rate = 0.2

    # Calculate the number of nickels received in exchange for the quarters
    nickels = 20 * 4

    # Calculate the number of iron nickels
    iron_nickels = nickels * exchange_rate

    # Calculate the value of the iron nickels
    iron_nickels_value = iron_nickels * 3

    # Calculate the total value of the money
    total_value = quarters_value + (nickels - iron_nickels) * 0.05 + iron_nickels_value

    result = total_value
    return result

print(solution())