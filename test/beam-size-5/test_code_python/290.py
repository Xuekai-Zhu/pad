def solution():
    
    total_oranges = 15
    oldest_son_age = 8
    youngest_son_age = oldest_son_age / 2
    remaining_oranges = total_oranges - oldest_son_age - youngest_son_age
    result = remaining_oranges
    return result

print(solution())