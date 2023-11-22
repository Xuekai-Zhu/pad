def solution():
    
    # Define the price and quantity of lemonade sold in each hour
    LEMONADE_PRICE = 0.5
    LEMONADE_QUANTITY = 15
    LEMONADE_QUANTITY = 10

    # Define the number of hours Patrick sold lemonade for
    hours_sold = 6

    # Calculate the total earnings from selling lemonade for the first 4 hours
    earnings_first_4_hours = LEMONADE_PRICE * hours_sold

    # Calculate the total earnings from selling lemonade for the next 2 hours
    earnings_second_2_hours = LEMONADE_PRICE * hours_sold

    # Calculate the total earnings from selling lemonade for 6 hours
    total_earnings = earnings_first_4_hours + earnings_second_2_hours

    # Display the total earnings
    result = total_earnings
    return result

print(solution())