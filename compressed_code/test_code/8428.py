def solution():
    
    adults_on_bikes = 6
    children_on_trikes = 15
    wheels_on_bikes = 2
    wheels_on_trikes = 3
    total_wheels = (adults_on_bikes * wheels_on_bikes) + (children_on_trikes * wheels_on_trikes)
    result = total_wheels
    return result

print(solution())