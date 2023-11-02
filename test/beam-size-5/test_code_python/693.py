def solution():
    num_children = 3
    num_grandchildren_per_child = 3
    num_babies_per_grandchild = 3

    # Calculate the total number of grandchildren
    total_grandchildren = num_children * num_grandchildren_per_child

    # Calculate the total number of babies
    total_babies = total_grandchildren * num_babies_per_grandchild

    # Calculate the number of great grand-babies
    num_great_grand_babies = total_babies - total_grandchildren
    result = num_great_grand_babies
    return result

print(solution())