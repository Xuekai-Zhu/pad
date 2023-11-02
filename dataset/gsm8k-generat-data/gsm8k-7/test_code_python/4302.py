def solution():
    hot_dogs_per_day = 60
    pizzas_per_day = hot_dogs_per_day + 40
    days_in_June = 30

    # Calculate the total number of hot dogs made in June
    total_hot_dogs = hot_dogs_per_day * days_in_June

    # Calculate the total number of pizzas made in June
    total_pizzas = pizzas_per_day * days_in_June

    result = (total_pizzas, total_hot_dogs)
    return result

print(solution())