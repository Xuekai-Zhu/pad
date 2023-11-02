def solution():
    
    num_classrooms = 15
    num_big_classrooms = num_classrooms // 3
    num_small_classrooms = num_classrooms - num_big_classrooms
    big_classroom_capacity = 30
    small_classroom_capacity = 25
    total_capacity = (num_big_classrooms * big_classroom_capacity) + (num_small_classrooms * small_classroom_capacity)
    result = total_capacity
    return result

print(solution())