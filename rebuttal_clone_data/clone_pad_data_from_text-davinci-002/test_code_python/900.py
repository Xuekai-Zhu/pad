def solution():
    active_squirrels = 2
    lazy_squirrel = 1
    days = 40
    active_squirrels_daily_nut_total = active_squirrels * 30
    lazy_squirrel_daily_nut_total = lazy_squirrel * 20
    total_nuts = (active_squirrels_daily_nut_total + lazy_squirrel_daily_nut_total) * days
    result = total_nuts
    return result

print(solution())