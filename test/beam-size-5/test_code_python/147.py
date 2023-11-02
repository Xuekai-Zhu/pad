def solution():
    tire_cost = 0.25
    num_bicycles = 5
    num_tricycle_people = 3
    num_unicycle_people = 1

    # Calculate the total number of tires inflated
    total_tires = num_bicycles * tire_cost

    # Calculate the total number of tricycle tires
    total_tricycle_tires = num_tricycle_people * tire_cost

    # Calculate the total number of unicycle tires
    total_unicycle_tires = num_unicycle_people

    # Calculate the total amount of inflated
    total_inflated = total_tires + total_tricycle_tires + total_unicycle_tires
    result = total_inflated
    return result

print(solution())