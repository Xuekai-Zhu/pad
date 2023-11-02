def solution():
    spokes_front_wheel = 20  # Number of spokes on the front wheel
    spokes_back_wheel = 2 * spokes_front_wheel  # Number of spokes on the back wheel

    # Total number of spokes on the bicycle
    total_spokes = spokes_front_wheel + spokes_back_wheel
    result = total_spokes
    return result

print(solution())