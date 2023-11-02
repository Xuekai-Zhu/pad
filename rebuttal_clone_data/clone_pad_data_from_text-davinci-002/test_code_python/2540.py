def solution():
    initial_price = 4000
   time_in_years = 3
    percent_increase = 300
    increase_amount = initial_price * (percent_increase / 100)
    future_price = increase_amount + initial_price
    result = future_price - initial_price
    return result

print(solution())