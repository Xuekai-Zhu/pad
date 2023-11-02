def solution():
    """Granger went to the grocery store. He saw that the Spam is $3 per can, the peanut butter is $5 per jar, and the bread is $2 per loaf. If he bought 12 cans of spam, 3 jars of peanut butter, and 4 loaves of bread, how much is the total amount he paid?"""
    # Define the price of each item
    spam_price = 3
    peanut_butter_price = 5
    bread_price = 2

    # Define the number of items bought
    spam_count = 12
    peanut_butter_count = 3
    bread_count = 4

    # Calculate the total cost of each item
    spam_total = spam_price * spam_count
    peanut_butter_total = peanut_butter_price * peanut_butter_count
    bread_total = bread_price * bread_count

    # Calculate the total cost of the purchase
    total_cost = spam_total + peanut_butter_total + bread_total

    # return the result
    result = total_cost
    return result

print(solution())