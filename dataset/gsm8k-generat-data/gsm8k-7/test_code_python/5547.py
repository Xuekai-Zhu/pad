def solution():
    num_on_tree = 5
    num_on_ground = 8
    num_eaten_by_dog = 3

    # Calculate the total number of apples left
    total_apples = num_on_tree + num_on_ground - num_eaten_by_dog
    result = total_apples
    return result

print(solution())