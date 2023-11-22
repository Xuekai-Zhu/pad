def solution():
    
    # Define the prices of chips and candy bars
    CHIPS_PRICE = 40
    CANDY_PRICE = 75

    # Define the total amount spent and the amount spent on bags of chips
    total_spent = 5
    chips_cost = CHIPS_PRICE * 3

    # Calculate the amount left after buying the chips
    money_left = total_spent - chips_cost

    # Calculate the number of candy bars bought
    candy_bars = money_left / CANDY_PRICE

    # Display the number of candy bars bought
    result = candy_bars
    return result

print(solution())