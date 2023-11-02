def solution():
    breakfast_muffin = 2
    breakfast_coffee = 4
    lunch_soup = 3
    lunch_salad = 5.25
    lunch_lemonade = 0.75
    breakfast_total = breakfast_muffin + breakfast_coffee
    lunch_total = lunch_soup + lunch_salad + lunch_lemonade
    difference = lunch_total - breakfast_total
    result = difference
    return result

print(solution())