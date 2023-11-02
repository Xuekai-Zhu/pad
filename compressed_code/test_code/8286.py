def solution():
    
    total_slices = 6 * 18
    cheese_slices = 8
    onion_slices = 4
    slices_eaten = cheese_slices + onion_slices
    slices_per_student = 2 + 1
    total_students = (total_slices - cheese_slices - onion_slices) // slices_per_student
    result = total_students
    return result

print(solution())