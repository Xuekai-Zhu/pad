def solution():
    initial_age = 7
    sister_age = 9
    target_age = 56
    current_age = initial_age + sister_age
    difference = target_age - current_age
    final_age = difference + initial_age
    
    return final_age

print(solution())