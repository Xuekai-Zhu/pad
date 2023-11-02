def solution():
    """Damien created a currency based on bottle caps and got his friends to take part. He finds 10 bottle caps a day on his way home and each bottle cap is worth $.25. How much money does he make in a 30 day month?"""
    bottle_caps_per_day = 10
    value_per_bottle_cap = 0.25
    days_per_month = 30
    total_value = bottle_caps_per_day * value_per_bottle_cap * days_per_month
    result = total_value
    return result

print(solution())