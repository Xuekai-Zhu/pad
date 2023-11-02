def solution():
    """Tas and his friends put up a t-shirt for sale. They ended up selling 200 t-shirts in 25 minutes. Half of the shirts were black and cost $30, while the other half were white and cost $25. How much money did they make per minute during the sale?"""
    total_t_shirts = 200
    black_t_shirts = total_t_shirts / 2
    white_t_shirts = total_t_shirts / 2
    black_t_shirt_price = 30
    white_t_shirt_price = 25
    total_money = (black_t_shirts * black_t_shirt_price) + (white_t_shirts * white_t_shirt_price)
    total_minutes = 25
    money_per_minute = total_money / total_minutes
    result = money_per_minute
    return result

print(solution())