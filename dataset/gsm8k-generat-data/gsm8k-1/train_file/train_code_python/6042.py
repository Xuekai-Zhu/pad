def solution():
    """Carlos has some gold quarters. If he spends them in a store, they are worth the regular amount. If he melts them down, he can get $100 per ounce. Each quarter weighs 1/5 of an ounce. How many times more money would he get from melting them down instead of spending them in a store?"""
    value_spent = 0.25
    weight_per_quarter = 1/5
    value_melted = 100 * weight_per_quarter
    times_more_money = value_melted / value_spent
    result = times_more_money
    return result

print(solution())