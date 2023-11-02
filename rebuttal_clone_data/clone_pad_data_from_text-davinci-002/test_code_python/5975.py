def solution():
    cups_per_day_per_dog = 6
    days_per_month = 30
    cups_per_month_per_dog = cups_per_day_per_dog * days_per_month
    weight_of_one_cup = 0.25
    weight_of_food_per_month_per_dog = weight_of_one_cup * cups_per_month_per_dog
    number_of_dogs = 2
    total_weight_of_food_per_month = weight_of_food_per_month_per_dog * number_of_dogs
    weight_of_bag = 20
    number_of_bags_per_month = total_weight_of_food_per_month / weight_of_bag
    result = number_of_bags_per_month
    return result

print(solution())