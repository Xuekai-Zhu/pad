def solution():
    
    white_bread_price = 3.5
    baguette_price = 1.5
    sourdough_bread_price = 4.5
    croissant_price = 2.0

    weekly_cost = (2 * white_bread_price) + baguette_price + (2 * sourdough_bread_price) + croissant_price
    total_cost = weekly_cost * 4

    result = total_cost
    return result

print(solution())