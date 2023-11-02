def solution():
    bikes = 4  # Billy's family owns 4 bicycles
    spokes_per_wheel = 10  # Each bicycle wheel has 10 spokes

    # Calculate the total number of spokes in the garage
    total_spokes = bikes * 2 * spokes_per_wheel  # Each bike has 2 wheels

    result = total_spokes
    return result

print(solution())