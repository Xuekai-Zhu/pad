def solution():
    """John decides to stop delivering the newspapers he is supposed to deliver and instead steals them to recycle them for cash. The Monday-Saturday papers weigh 8 ounces each. The Sunday paper weighs twice as much. He is supposed to deliver 250 papers a day. He doesn't deliver them for 10 weeks. If one ton of paper recycles for $20, how much did he make?"""
    weight_weekday = 8 * 6  # ounces of paper in a weekday
    weight_sunday = 8 * 2  # ounces of paper in a Sunday
    total_weight = weight_weekday * 6 + weight_sunday * 1  # ounces of paper in a week
    total_weight *= 10  # ounces of paper for 10 weeks
    total_weight /= 16  # pounds of paper for 10 weeks
    total_weight /= 2000  # tons of paper for 10 weeks
    price_per_ton = 20  # dollars per ton of paper
    total_income = total_weight * price_per_ton
    result = total_income
    return result

print(solution())