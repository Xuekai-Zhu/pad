def solution():
    bicycles = 50  # Wynter counted 50 bicycles
    tricycles = 20  # Wynter counted 20 tricycles
    wheels_per_bicycle = 2  # Each bicycle has 2 wheels
    wheels_per_tricycle = 3  # Each tricycle has 3 wheels

    # Calculate the total number of wheels
    total_wheels = (bicycles * wheels_per_bicycle) + (tricycles * wheels_per_tricycle)
    result = total_wheels
    return result

print(solution())