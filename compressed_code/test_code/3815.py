def solution():
    
    first_tree = 1000
    second_tree = first_tree / 2
    third_tree = first_tree / 2
    fourth_tree = first_tree + 200
    total_height = first_tree + second_tree + third_tree + fourth_tree
    average_height = total_height / 4
    result = average_height
    return result

print(solution())