def solution():
    burger = 5
    fries = 3
    drink = 3
    burger_meal = 9.5
    kid_burger = 3
    kid_fries = 2
    kid_drink = 2
    kid_meal = 5
    num_adult_meals = 2
    num_kid_meals = 2
    num_kids = 4
    adult_meal_cost = num_adult_meals * burger_meal
    kids_meal_cost = num_kid_meals * kid_meal
    total_meal_cost = adult_meal_cost + kids_meal_cost
    adult_food_cost = num_adult_meals * (burger + fries + drink)
    kids_food_cost = num_kids * (kid_burger + kid_fries + kid_drink)
    total_food_cost = adult_food_cost + kids_food_cost
    result = total_food_cost - total_meal_cost
    return result

print(solution())