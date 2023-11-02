def solution():
    hot_dogs_per_day = 60
    pizzas_per_day = hot_dogs_per_day + 40
    total_days_in_june = 30
    total_hot_dogs_in_june = hot_dogs_per_day * total_days_in_june
    total_pizzas_in_june = pizzas_per_day * total_days_in_june
    result = "The restaurant will make {} hot dogs and {} pizzas in June.".format(total_hot_dogs_in_june, total_pizzas_in_june)
    return result

print(solution())