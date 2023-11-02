def solution():
    num_cars = 16
    growth_rate = 1.5 #50% increase
    num_years = 3

    #Calculate the number of cars Bobby will have after three years
    num_cars_after_three_years = num_cars*(growth_rate**num_years)

    result = num_cars_after_three_years
    return result

print(solution())