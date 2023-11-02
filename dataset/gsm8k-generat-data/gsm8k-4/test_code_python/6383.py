def solution():
    """Troy makes soup. He buys 4 pounds of beef and 6 pounds of vegetables. The vegetables cost $2 per pound and the beef is 3 times that price. How much does everything cost?"""
    # Define the price of vegetables and calculate the price of beef
    VEG_PRICE = 2
    BEEF_PRICE = 3 * VEG_PRICE

    # Define the amount of beef and vegetables
    beef_amount = 4
    veg_amount = 6

    # Calculate the cost of the beef and vegetables
    beef_cost = beef_amount * BEEF_PRICE
    veg_cost = veg_amount * VEG_PRICE

    # Calculate the total cost
    total_cost = beef_cost + veg_cost

    # return the result
    result = total_cost
    return result

print(solution())