def solution():
    
    cost_of_trip = 485
    grandma_payment = 250
    amount_to_earn = cost_of_trip - grandma_payment
    profit_per_candy_bar = 1.25
    bars_to_sell = amount_to_earn / profit_per_candy_bar
    result = bars_to_sell
    return result

print(solution())