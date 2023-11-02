def solution():
    
    num_sandwiches = 20
    portions_per_sandwich = 4
    total_portions = num_sandwiches * portions_per_sandwich
    num_people = total_portions // 8
    result = num_people
    return result

print(solution())