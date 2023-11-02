def solution():
    """Granger went to the grocery store. He saw that the Spam is $3 per can, the peanut butter is $5 per jar, and the bread is $2 per loaf. If he bought 12 cans of spam, 3 jars of peanut butter, and 4 loaves of bread, how much is the total amount he paid?"""
    # Define the cost of each item
    SPAM_PRICE = 3
    PEANUT_BUTTER_PRICE = 5
    BREAD_PRICE = 2

    # Define the quantity of each item purchased
    spam_quantity = 12
    peanut_butter_quantity = 3
    bread_quantity = 4

    # Calculate the total cost of the spam
    spam_cost = spam_quantity * SPAM_PRICE

    # Calculate the total cost of the peanut butter
    peanut_butter_cost = peanut_butter_quantity * PEANUT_BUTTER_PRICE

    # Calculate the total cost of the bread
    bread_cost = bread_quantity * BREAD_PRICE

    # Calculate the total amount paid
    total_cost = spam_cost + peanut_butter_cost + bread_cost

    # Display the total amount paid
    result = total_cost
    return result

print(solution())