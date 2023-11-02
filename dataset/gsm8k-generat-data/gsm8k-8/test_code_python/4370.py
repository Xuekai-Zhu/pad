def solution():
    # Calculate the initial number of apples picked by each person
    initial_pick = 400

    # Calculate the second pick, which is 3/4 of the initial pick
    second_pick = 0.75 * initial_pick

    # Calculate the total number of apples picked by each person
    total_pick = initial_pick + second_pick

    # Calculate the number of apples needed to reach the target
    remaining_pick = 600

    # Calculate the target number of apples
    target = (2 * initial_pick) + (remaining_pick / 0.75)

    result = target
    return result

print(solution())