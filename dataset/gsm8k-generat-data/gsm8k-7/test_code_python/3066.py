def solution():
    num_oranges = 50
    orange_to_lime_ratio = 2  # Martin had twice as many oranges as limes after eating half of his fruits

    # Calculate the total number of fruits Martin had before eating half
    total_fruits = num_oranges / orange_to_lime_ratio

    # Calculate the initial number of fruits Martin had
    initial_fruits = total_fruits * 2
    result = initial_fruits
    return result

print(solution())