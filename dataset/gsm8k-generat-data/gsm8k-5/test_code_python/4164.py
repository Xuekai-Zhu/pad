def solution():
    cucumber_price = 5  # One kilogram of cucumbers costs $5
    tomato_price = cucumber_price * 0.8  # One kilogram of tomatoes is 20% cheaper than one kilogram of cucumbers

    # Calculate the total price of two kilograms of tomatoes and three kilograms of cucumbers
    total_price = (2 * tomato_price) + (3 * cucumber_price)
    result = total_price
    return result

print(solution())