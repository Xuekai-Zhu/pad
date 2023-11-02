def solution():
    """Carlos has some gold quarters. If he spends them in a store, they are worth the regular amount. If he melts them down, he can get $100 per ounce. Each quarter weighs 1/5 of an ounce. How many times more money would he get from melting them down instead of spending them in a store?"""
    gold_quarters_weight = 0.2  # 1/5 of an ounce
    melt_down_value = 100  # per ounce
    regular_value = 0.25  # face value of a quarter

    melt_down_money = melt_down_value / gold_quarters_weight
    regular_money = regular_value

    times_more = melt_down_money / regular_money
    result = times_more
    return result

print(solution())