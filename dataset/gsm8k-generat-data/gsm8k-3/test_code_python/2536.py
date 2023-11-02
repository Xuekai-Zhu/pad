def solution():
    """To earn money for her new computer, Tina sells handmade postcards. In a day, she can make 30 such postcards. For each postcard sold, Tina gets $5. How much money did Tina earn if she managed to sell all the postcards she made every day for 6 days?"""
    # Define the number of postcards made each day and the price per postcard
    POSTCARDS_PER_DAY = 30
    PRICE_PER_POSTCARD = 5

    # Calculate the total number of postcards made and sold
    total_postcards = POSTCARDS_PER_DAY * 6

    # Calculate Tina's earnings
    earnings = total_postcards * PRICE_PER_POSTCARD

    # Display Tina's earnings
    result = earnings
    return result

print(solution())