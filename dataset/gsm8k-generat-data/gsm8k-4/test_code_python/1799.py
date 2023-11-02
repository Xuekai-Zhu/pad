def solution():
    """Silvia wants to buy a new guitar online. The price of the guitar has a suggested retail price of $1000. Guitar Center has a special deal of 15% off but has a shipping fee of $100. Sweetwater has a 10% off deal with free shipping. How much will she save by buying from the cheaper store compared to the other store?"""
    # Define the original price of the guitar
    original_price = 1000

    # Calculate the price after the Guitar Center deal
    guitar_center_price = original_price * 0.85 + 100

    # Calculate the price after the Sweetwater deal
    sweetwater_price = original_price * 0.9

    # Calculate the amount saved by buying from Sweetwater
    savings = guitar_center_price - sweetwater_price

    result = savings
    return result

print(solution())