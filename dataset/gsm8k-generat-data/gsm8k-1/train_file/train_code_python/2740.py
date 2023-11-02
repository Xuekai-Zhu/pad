def solution():
    """Zoe wants to go on the field trip to Washington DC with her middle school this spring and the cost is $485. Her grandma gave her $250 toward her fees and she must earn the rest by selling candy bars. She makes $1.25 for every candy bar she sells. How many candy bars does Zoe need to sell to earn the money for the trip?"""
    cost_of_trip = 485
    grandma_payment = 250
    amount_to_earn = cost_of_trip - grandma_payment
    profit_per_candy_bar = 1.25
    bars_to_sell = amount_to_earn / profit_per_candy_bar
    result = bars_to_sell
    return result

print(solution())