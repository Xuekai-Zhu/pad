def solution():
    # Calculate the total distance Allyn hit the ball from the starting tee to the hole
    first_turn_distance = 180
    second_turn_distance = first_turn_distance / 2
    third_turn_distance = second_turn_distance + 20
    total_distance = first_turn_distance + second_turn_distance + third_turn_distance
    result = total_distance
    return result

print(solution())