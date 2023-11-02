def solution():
    
    trip_cost = 485
    grandma_contribution = 250
    money_to_earn = trip_cost - grandma_contribution
    price_per_candy_bar = 1.25
    candy_bars_to_sell = money_to_earn / price_per_candy_bar
    result = candy_bars_to_sell
    return result

print(solution())