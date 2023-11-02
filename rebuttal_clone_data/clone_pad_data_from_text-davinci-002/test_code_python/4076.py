def solution():
    number_of_goldfish = 50
    ounces_of_food_per_day = 1.5
    percent_of_goldfish = 20
    number_of_goldfish_special_food = number_of_goldfish * (percent_of_goldfish / 100)
    ounces_of_special_food_per_day = ounces_of_food_per_day * 1.25
    cost_of_special_food_per_day = 3 * ounces_of_special_food_per_day
    cost_of_special_food_per_week = cost_of_special_food_per_day * 7
    result = cost_of_special_food_per_week
    return result

print(solution())