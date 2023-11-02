def solution():
    """Jackie loves to climb trees. She climbed a 1000 foot tall tree. Then she climbed 2 trees that were half as tall as the first tree. She finished by climbing a tree that was 200 feet taller than her first tree. What was the average height of the trees that Jackie climbed?"""
    first_tree = 1000
    second_tree = first_tree / 2
    third_tree = first_tree / 2
    fourth_tree = first_tree + 200
    total_height = first_tree + second_tree + third_tree + fourth_tree
    average_height = total_height / 4
    result = average_height
    return result

print(solution())