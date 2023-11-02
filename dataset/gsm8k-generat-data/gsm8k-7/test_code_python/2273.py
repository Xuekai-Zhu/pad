def solution():
    pasture_rental_cost = 500 * 12  # cost per month * number of months in a year
    food_cost = 10 * 365  # cost per day * number of days in a year
    lesson_cost = 60 * 2 * 52  # cost per lesson * number of lessons per week * number of weeks in a year

    total_cost = pasture_rental_cost + food_cost + lesson_cost
    result = total_cost
    return result

print(solution())