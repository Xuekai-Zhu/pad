def solution():
    # Define the amount of water each sibling drinks in a day
    theo_daily = 8
    mason_daily = 7
    roxy_daily = 9

    # Calculate the total amount of water each sibling drinks in a week
    theo_weekly = theo_daily * 7
    mason_weekly = mason_daily * 7
    roxy_weekly = roxy_daily * 7

    # Calculate the total amount of water the siblings drink together in a week
    total_weekly = theo_weekly + mason_weekly + roxy_weekly
    result = total_weekly
    return result

print(solution())