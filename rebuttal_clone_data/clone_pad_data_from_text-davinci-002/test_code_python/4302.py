def solution():
    pizzas_per_day = 60 + 40
    hot_dogs_per_day = 60
    days_in_june = 30
    total_pizzas = pizzas_per_day * days_in_june
    total_hot_dogs = hot_dogs_per_day * days_in_june
    
    result = "In June, the restaurant will make {} pizzas and {} hot dogs.".format(total_pizzas, total_hot_dogs)
    return result

print(solution())