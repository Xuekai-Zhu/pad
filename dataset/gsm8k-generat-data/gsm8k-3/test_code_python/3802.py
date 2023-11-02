def solution():
    """Claire won a $100 gift card to her favorite coffee shop. She wants to treat herself to a latte that cost $3.75 and a croissant for $3.50 every morning for a week.  She also plans to buy 5 cookies that cost $1.25 each. How much money will be left on her card after a week of coffee and pastry?"""
    # Define the cost of a latte and a croissant
    LATTE_COST = 3.75
    CROISSANT_COST = 3.50

    # Define the cost of a cookie and the number of cookies Claire will buy
    COOKIE_COST = 1.25
    NUM_COOKIES = 5

    # Calculate the total cost of Claire's daily order
    daily_order_cost = LATTE_COST + CROISSANT_COST + (COOKIE_COST * NUM_COOKIES)

    # Calculate the total cost of Claire's order for the week
    weekly_order_cost = daily_order_cost * 7

    # Calculate the amount left on Claire's gift card after the week
    remaining_balance = 100 - weekly_order_cost

    # Display the remaining balance
    result = remaining_balance
    return result

print(solution())