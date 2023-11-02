def solution():
    # Calculate the total number of tires on the vehicles Juan saw
    cars_tires = 15*4  # each car has 4 tires
    bicycles_tires = 3*2  # each bicycle has 2 tires
    pickup_trucks_tires = 8*4  # each pickup truck has 4 tires
    tricycle_tires = 1*3  # the tricycle has 3 tires
    total_tires = cars_tires + bicycles_tires + pickup_trucks_tires + tricycle_tires
    result = total_tires
    return result

print(solution())