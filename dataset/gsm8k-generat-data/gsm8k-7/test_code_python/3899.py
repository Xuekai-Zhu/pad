def solution():
    total_fruit = 56

    # Calculate the number of oranges in the box
    num_oranges = total_fruit / 4

    # Calculate the number of peaches in the box
    num_peaches = num_oranges / 2

    # Calculate the number of apples in the box
    num_apples = num_peaches * 5
    result = num_apples
    return result

print(solution())