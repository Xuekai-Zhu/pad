def solution():
    
    burrito_cost = 6
    burrito_count = 10
    burrito_calories = 120
    burger_cost = 8
    burger_count = 5
    burger_calories = 400
    burrito_cal_per_dollar = (burrito_count * burrito_calories) / burrito_cost
    burger_cal_per_dollar = (burger_count * burger_calories) / burger_cost
    difference = burger_cal_per_dollar - burrito_cal_per_dollar
    result = difference
    return result

print(solution())