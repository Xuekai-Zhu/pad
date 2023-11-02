def solution():
    # Calculate the cost of the Legos set
    total_cars = 3
    total_earnings = 45
    cost_per_car = 5
    cost_of_cars = total_cars * cost_per_car
    cost_of_legos = total_earnings - cost_of_cars
    result = cost_of_legos
    return result

print(solution())