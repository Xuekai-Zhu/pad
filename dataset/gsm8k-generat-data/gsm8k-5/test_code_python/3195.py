def solution():
    sodas_per_pack = 12  # Each pack of soda has 12 sodas
    packs_bought = 5  # James buys 5 packs of sodas
    sodas_total = sodas_per_pack * packs_bought + 10  # James had 10 sodas already

    days_in_week = 7  # There are 7 days in a week
    sodas_per_day = sodas_total / days_in_week  # James finishes all sodas in 1 week

    result = sodas_per_day
    return result

print(solution())