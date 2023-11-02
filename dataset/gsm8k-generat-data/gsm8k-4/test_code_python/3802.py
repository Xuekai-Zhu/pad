def solution():
    """Claire won a $100 gift card to her favorite coffee shop. She wants to treat herself to a latte that cost $3.75 and a croissant for $3.50 every morning for a week. She also plans to buy 5 cookies that cost $1.25 each. How much money will be left on her card after a week of coffee and pastry?"""
    # Define the prices of a latte, croissant and cookies
    LATTE_PRICE = 3.75
    CROISSANT_PRICE = 3.50
    COOKIE_PRICE = 1.25

    # Calculate the total cost of Claire's breakfast for a week
    breakfast_cost = (LATTE_PRICE + CROISSANT_PRICE) * 7 + COOKIE_PRICE * 5

    # Calculate the money left on her gift card after a week
    remaining_money = 100 - breakfast_cost

    # return the result
    result = remaining_money
    return result

print(solution())