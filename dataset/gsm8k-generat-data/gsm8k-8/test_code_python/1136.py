def solution():
    # Calculate the total amount of food needed for all dogs during one day
    daily_food_per_dog = 250
    total_food_per_day = daily_food_per_dog * 4

    # Calculate the total amount of food needed for all dogs during the vacation
    vacation_days = 14
    total_food_during_vacation = total_food_per_day * vacation_days

    # Convert the total amount of food to kilograms
    total_food_in_kgs = total_food_during_vacation / 1000
    result = total_food_in_kgs
    return result

print(solution())