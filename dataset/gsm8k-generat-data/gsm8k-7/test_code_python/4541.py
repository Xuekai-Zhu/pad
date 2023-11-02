def solution():
    rise_time = 120
    num_rises = 2
    knead_time = 10
    bake_time = 30

    # Calculate the total rise time
    total_rise_time = rise_time * num_rises

    # Calculate the total time it takes to make the bread
    total_time = total_rise_time + knead_time + bake_time
    result = total_time
    return result

print(solution())