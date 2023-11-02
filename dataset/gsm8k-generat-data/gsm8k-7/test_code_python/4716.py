def solution():
    num_bicycles = 3
    num_tricycles = 4
    num_unicycles = 7

    # Calculate the total number of wheels from the bicycles
    total_bicycle_wheels = num_bicycles * 2

    # Calculate the total number of wheels from the tricycles
    total_tricycle_wheels = num_tricycles * 3

    # Calculate the total number of wheels from the unicycles
    total_unicycle_wheels = num_unicycles * 1

    # Calculate the total number of wheels
    total_wheels = total_bicycle_wheels + total_tricycle_wheels + total_unicycle_wheels
    result = total_wheels
    return result

print(solution())