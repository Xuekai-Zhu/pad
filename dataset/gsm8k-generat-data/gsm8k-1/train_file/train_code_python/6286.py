def solution():
    """John can produce 1000 tires a day. It cost $250 to produce each tire. He manages to sell them for 1.5 times as much. He could sell 1200 tires a day if his factory was able to produce more. How much money does he lose out a week by not being able to produce all the tires?"""
    tires_per_day = 1000
    cost_per_tire = 250
    sale_price_per_tire = cost_per_tire * 1.5
    max_tires_per_day = 1200
    tires_not_produced_per_day = max_tires_per_day - tires_per_day
    money_lost_per_day = tires_not_produced_per_day * sale_price_per_tire - tires_not_produced_per_day * cost_per_tire
    result = money_lost_per_day * 7
    return result

print(solution())