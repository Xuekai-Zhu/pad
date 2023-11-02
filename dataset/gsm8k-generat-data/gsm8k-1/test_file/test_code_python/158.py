def solution():
    """If a bag of marbles costs $20 and the price increases by 20% of the original price every two months, how much would a bag of marbles cost after 36 months?"""
    original_price = 20
    time_interval = 2 # months
    price_increase_percent = 20 # percent
    total_time = 36 # months
    num_increases = total_time // time_interval
    final_price = original_price * ((1 + (price_increase_percent / 100)) ** num_increases)
    result = final_price
    return result

print(solution())