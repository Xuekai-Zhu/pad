def solution():
    
    first_week = 20
    second_week = int(2/5 * first_week)
    third_week = 2 * second_week
    fourth_week = first_week + 10
    total_puppies = first_week + second_week + third_week + fourth_week
    result = total_puppies
    return result

print(solution())