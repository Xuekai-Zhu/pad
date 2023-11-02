def solution():
    """One kilogram of tomatoes is 20% cheaper than one kilogram of cucumbers. One kilogram of cucumbers costs $5. What is the price of two kilograms of tomatoes and three kilograms of cucumbers?"""
    cucumber_price = 5
    tomato_price = cucumber_price * 0.8
    total_price = (2 * tomato_price) + (3 * cucumber_price)
    result = total_price
    return result

print(solution())