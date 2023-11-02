def solution():
    sister_age = 2
    maxwell_age = sister_age * 2
    current_sister_age = sister_age + 2
    current_maxwell_age = current_sister_age * 2
    result = current_maxwell_age - maxwell_age
    return result

print(solution())