def solution():
    
    apple_count = 180
    plum_count = apple_count / 3
    total_fruits = apple_count + plum_count
    remaining_fruits = total_fruits * (2 / 5)
    remaining_apples = remaining_fruits * (3 / 4)
    remaining_plums = remaining_fruits * (1 / 4)
    result = remaining_apples + remaining_plums
    return result

print(solution())