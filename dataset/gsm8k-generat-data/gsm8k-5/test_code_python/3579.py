def solution():
    theo_daily = 8  # cups of water Theo drinks daily
    mason_daily = 7  # cups of water Mason drinks daily
    roxy_daily = 9  # cups of water Roxy drinks daily
    days_per_week = 7  # number of days in a week

    # Calculate total cups of water drank by the siblings in a week
    total_weekly = (theo_daily + mason_daily + roxy_daily) * days_per_week

    result = total_weekly
    return result

print(solution())