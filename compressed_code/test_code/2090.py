def solution():
    
    friday_magazines = 8
    saturday_magazines = 12
    sunday_magazines = 4 * friday_magazines
    total_magazines = friday_magazines + saturday_magazines + sunday_magazines - 4
    result = total_magazines
    return result

print(solution())