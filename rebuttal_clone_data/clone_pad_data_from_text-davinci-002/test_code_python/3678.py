def solution():
    initial_height = 5
    growth_rate = 3
    target_height = 23
    current_age = 1
    while current_height < target_height:
        current_height += growth_rate
        current_age += 1
    result = current_age
    return result

print(solution())