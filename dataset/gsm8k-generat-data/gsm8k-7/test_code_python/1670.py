def solution():
    total_fruit = 40
    num_apples = 3
    num_oranges = 1

    # Calculate the ratio of apples to oranges
    total_num_fruit = num_apples + num_oranges
    apple_ratio = num_apples / total_num_fruit
    orange_ratio = num_oranges / total_num_fruit

    # Calculate the number of oranges based on the ratio and total fruit capacity
    num_oranges = int(orange_ratio * total_fruit)
    result = num_oranges
    return result

print(solution())