def solution():
    num_bicycles = 4
    num_spokes_per_wheel = 10
    num_wheels_per_bicycle = 2

    # Calculate the total number of wheels in the garage
    total_wheels = num_bicycles * num_wheels_per_bicycle

    # Calculate the total number of spokes in the garage
    total_spokes = total_wheels * num_spokes_per_wheel
    result = total_spokes
    return result

print(solution())