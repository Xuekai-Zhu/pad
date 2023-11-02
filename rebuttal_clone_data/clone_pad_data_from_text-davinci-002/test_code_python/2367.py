def solution():
    meals_prepared_lunch = 17
    meals_sold_lunch = 12
    meals_prepared_dinner = 5
    meals_remaining_lunch = meals_prepared_lunch - meals_sold_lunch
    meals_for_dinner = meals_prepared_dinner + meals_remaining_lunch
    result = meals_for_dinner
    return result

print(solution())