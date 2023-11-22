def solution():
    
    flowers_per_day = 2
    days_passed = 15
    flowers_grown = flowers_per_day * days_passed
    flowers_left = flowers_grown - 5
    total_flowers = flowers_grown + flowers_left
    result = total_flowers
    return result

print(solution())