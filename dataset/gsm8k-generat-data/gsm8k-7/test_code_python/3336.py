def solution():
    num_bicycles = 6
    num_tricycles = 15

    # Calculate the total number of wheels on all bicycles
    total_bicycle_wheels = num_bicycles * 2

    # Calculate the total number of wheels on all tricycles
    total_tricycle_wheels = num_tricycles * 3

    # Calculate the total number of wheels that Dimitri saw at the park
    total_wheels = total_bicycle_wheels + total_tricycle_wheels
    result = total_wheels
    return result

print(solution())