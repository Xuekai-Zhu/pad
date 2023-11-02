def solution():
    """Bernie has a collection of 18 unique postcards. He decided to sell half his collection for $15 per postcard. After he has successfully sold his postcards he decided to spend all the earned money to buy new postcards for $5 each. How many postcards does Bernie have after all his transactions?"""
    # Define the number of postcards Bernie has
    num_postcards = 18

    # Define the selling price per postcard and the price for new postcards
    selling_price = 15
    new_price = 5

    # Calculate the number of postcards Bernie sells and his earnings
    num_sold = num_postcards // 2
    earnings = num_sold * selling_price

    # Calculate the number of new postcards Bernie can buy
    num_new = earnings // new_price

    # Calculate the total number of postcards Bernie has after all transactions
    total_num_postcards = num_postcards - num_sold + num_new

    # Display the total number of postcards
    result = total_num_postcards
    return result

print(solution())