def solution():
    # Calculate the total number of wheels from bicycles
    num_bicycle_wheels = 6 * 2  # 6 adults riding bicycles, each bicycle has 2 wheels

    # Calculate the total number of wheels from tricycles
    num_tricycle_wheels = 15 * 3  # 15 children riding tricycles, each tricycle has 3 wheels

    # Calculate the total number of wheels Dimitri saw at the park
    total_wheels = num_bicycle_wheels + num_tricycle_wheels
    result = total_wheels
    return result

print(solution())