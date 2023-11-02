def solution():
    
    first_try = 400
    second_try = first_try - 70
    third_try = 2 * second_try
    total_points = first_try + second_try + third_try
    result = total_points
    return result

print(solution())