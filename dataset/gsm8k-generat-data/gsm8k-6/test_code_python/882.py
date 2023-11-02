def solution():
    # Calculate the total number of spokes on the bicycle
    front_spokes = 20
    back_spokes = 2 * front_spokes  # twice as many spokes on the back wheel as on the front wheel
    total_spokes = front_spokes + back_spokes
    result = total_spokes
    return result

print(solution())