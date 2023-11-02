def solution():
    theo_daily = 8
    mason_daily = 7
    roxy_daily = 9
    num_days = 7

    # Calculate the total amount of water each sibling drinks in one week
    theo_weekly = theo_daily * num_days
    mason_weekly = mason_daily * num_days
    roxy_weekly = roxy_daily * num_days

    # Calculate the total amount of water the siblings drink together in one week
    total_weekly = theo_weekly + mason_weekly + roxy_weekly
    result = total_weekly
    return result

print(solution())