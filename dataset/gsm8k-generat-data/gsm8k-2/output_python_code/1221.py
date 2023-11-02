def solution():
    """Wendy is a fruit vendor, and she sells an apple at $1.50 each and one orange at $1. In the morning, she was able to sell an average of 40 apples and 30 oranges. In the afternoon, she was able to sell 50 apples and 40 oranges. How much are her total sales for the day?"""
    apple_price = 1.5
    orange_price = 1
    morning_apples = 40
    morning_oranges = 30
    afternoon_apples = 50
    afternoon_oranges = 40
    morning_sales = (apple_price * morning_apples) + (orange_price * morning_oranges)
    afternoon_sales = (apple_price * afternoon_apples) + (orange_price * afternoon_oranges)
    total_sales = morning_sales + afternoon_sales
    result = total_sales
    return result

print(solution())