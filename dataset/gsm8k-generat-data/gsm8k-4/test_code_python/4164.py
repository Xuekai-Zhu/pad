def solution():
    """One kilogram of tomatoes is 20% cheaper than one kilogram of cucumbers. One kilogram of cucumbers costs $5. What is the price of two kilograms of tomatoes and three kilograms of cucumbers?"""
    # Define the price of one kilogram of cucumbers
    cucumber_price = 5

    # Calculate the price of one kilogram of tomatoes
    tomato_price = cucumber_price * 0.8

    # Calculate the price of two kilograms of tomatoes and three kilograms of cucumbers
    total_price = (2 * tomato_price) + (3 * cucumber_price)

    result = total_price
    return result

print(solution())