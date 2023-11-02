def solution():
    """Wendy is a fruit vendor, and she sells an apple at $1.50 each and one orange at $1. In the morning, she was able to sell an average of 40 apples and 30 oranges. In the afternoon, she was able to sell 50 apples and 40 oranges. How much are her total sales for the day?"""
    morning_apples = 40
    morning_oranges = 30
    afternoon_apples = 50
    afternoon_oranges = 40
    price_apples = 1.50
    price_oranges = 1
    total_sales = (morning_apples + afternoon_apples) * price_apples + (morning_oranges + afternoon_oranges) * price_oranges
    result = total_sales
    return result

print(solution())