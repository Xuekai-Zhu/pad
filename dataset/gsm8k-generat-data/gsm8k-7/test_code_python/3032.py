def solution():
    wednesday_harvest = 400
    thursday_harvest = wednesday_harvest / 2
    friday_harvest = 2000 - wednesday_harvest - thursday_harvest

    total_harvest = friday_harvest
    remaining_after_giving_away = total_harvest - 700
    result = remaining_after_giving_away
    return result

print(solution())