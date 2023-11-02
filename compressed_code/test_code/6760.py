def solution():
    
    initial_watermelons = 10 * 12
    sold_yesterday = initial_watermelons * 0.4
    remaining_today = initial_watermelons - sold_yesterday
    sold_today = remaining_today / 4
    left_to_sell = remaining_today - sold_today
    result = left_to_sell
    return result

print(solution())