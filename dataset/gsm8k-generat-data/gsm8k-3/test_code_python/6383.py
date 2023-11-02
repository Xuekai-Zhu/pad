def solution():
    """Troy makes soup.  He buys 4 pounds of beef and 6 pounds of vegetables.  The vegetables cost $2 per pound and the beef is 3 times that price.  How much does everything cost?"""
    # Define the price of vegetables and beef
    VEGETABLE_PRICE = 2
    BEEF_PRICE = 3 * VEGETABLE_PRICE

    # Define the amount of vegetables and beef purchased
    vegetable_pounds = 6
    beef_pounds = 4

    # Calculate the cost of the vegetables
    vegetable_cost = VEGETABLE_PRICE * vegetable_pounds

    # Calculate the cost of the beef
    beef_cost = BEEF_PRICE * beef_pounds

    # Calculate the total cost of the ingredients
    total_cost = vegetable_cost + beef_cost

    # Return the total cost
    result = total_cost
    return result

print(solution())