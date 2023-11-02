def solution():
    # Calculate the original number of oranges per student
    original_oranges_per_student = 108 // 12 

    # Calculate the number of oranges per student after throwing away bad oranges
    remaining_oranges = 108 - 36 
    remaining_oranges_per_student = remaining_oranges // 12 

    # Calculate the difference in oranges per student
    difference = original_oranges_per_student - remaining_oranges_per_student
    result = difference
    return result

print(solution())