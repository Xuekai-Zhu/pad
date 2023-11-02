def solution():
    """Jamie is in a walking group with 4 other ladies. The ladies all walk 3 miles together. On top of that, Jamie walks an additional 2 miles per day for 6 days while her friend Sue walks half that amount in 6 days. If they walk this same route 6 days a week, how many miles do the ladies walk in total?"""
    ladies_walk_group = 3
    jamie_extra_miles_per_day = 2
    sue_extra_miles_per_day = jamie_extra_miles_per_day / 2
    days_per_week = 6
    total_ladies_walk_miles = (ladies_walk_group + jamie_extra_miles_per_day) * days_per_week + (sue_extra_miles_per_day * days_per_week)
    result = total_ladies_walk_miles
    return result

print(solution())