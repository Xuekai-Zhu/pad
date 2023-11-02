def solution():
    
    # Define the initial stock price and the percentage increase in the first year
    initial_price = 8
    first_year_increase = 0.5

    # Calculate the new stock price after the first year
    new_stock_price = initial_price * (1 + first_year_increase)

    # Calculate the new stock price after the second year
    new_stock_price = new_stock_price * (1 - second_year_increase)

    # Calculate the final value of all 8 shares
    final_value = new_stock_price * 8

    # Display the final value of all 8 shares
    result = final_value
    return result

print(solution())