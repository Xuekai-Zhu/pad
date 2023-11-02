def solution():
    recommended_sugar_daily = 38
    sugar_per_doughnut = 10
    doughnuts_to_exceed = recommended_sugar_daily / sugar_per_doughnut
    if doughnuts_to_exceed > 4:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())