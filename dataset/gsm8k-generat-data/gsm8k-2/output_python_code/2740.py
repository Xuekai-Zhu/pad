def solution():
    """Zoe wants to go on the field trip to Washington DC with her middle school this spring and the cost is $485. Her grandma gave her $250 toward her fees and she must earn the rest by selling candy bars. She makes $1.25 for every candy bar she sells. How many candy bars does Zoe need to sell to earn the money for the trip?"""
    trip_cost = 485
    grandma_contribution = 250
    money_to_earn = trip_cost - grandma_contribution
    price_per_candy_bar = 1.25
    candy_bars_to_sell = money_to_earn / price_per_candy_bar
    result = candy_bars_to_sell
    return result

print(solution())