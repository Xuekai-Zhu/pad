def solution():
    num_potatoes = 96
    num_potatoes_made = 6
    num_browns_made = 36

    # Calculate the total number of potatoes that can be made
    total_potatoes = num_potatoes / num_potatoes_made

    # Calculate the total number of hash browns that can be made
    total_num_browns = total_potatoes * num_browns_made
    result = total_num_browns
    return result

print(solution())