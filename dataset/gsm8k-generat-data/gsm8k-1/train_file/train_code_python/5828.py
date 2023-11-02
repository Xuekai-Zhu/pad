def solution():
    """Tas and his friends put up a t-shirt for sale. They ended up selling 200 t-shirts in 25 minutes. Half of the shirts were black and cost $30, while the other half were white and cost $25. How much money did they make per minute during the sale?"""
    total_shirts = 200
    black_shirts = total_shirts / 2
    white_shirts = total_shirts / 2
    black_price = 30
    white_price = 25
    total_money = (black_shirts * black_price) + (white_shirts * white_price)
    time_in_minutes = 25
    money_per_minute = total_money / time_in_minutes
    result = money_per_minute
    return result

print(solution())