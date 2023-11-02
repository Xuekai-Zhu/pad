def solution():
    onions_chopped_per_minute = 15
    minutes = 5
    onions_chopped = onions_chopped_per_minute * minutes
    cals_onions_chopped_in_30_minutes = onions_chopped * 6
    result = cals_onions_chopped_in_30_minutes - onions_chopped
    return result

print(solution())