def solution():
    """Bernie has a collection of 18 unique postcards. He decided to sell half his collection for $15 per postcard. After he has successfully sold his postcards he decided to spend all the earned money to buy new postcards for $5 each. How many postcards does Bernie have after all his transactions?"""
    # Define the initial number of postcards
    num_postcards = 18

    # Calculate the number of postcards sold
    num_sold = num_postcards / 2

    # Calculate the earnings from selling the postcards
    earnings = num_sold * 15

    # Calculate the number of new postcards Bernie can buy with his earnings
    num_new = earnings / 5

    # Calculate the total number of postcards Bernie has after all his transactions
    total_postcards = num_postcards - num_sold + num_new

    # return the result
    result = total_postcards
    return result

print(solution())