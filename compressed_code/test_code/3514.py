def solution():
    
    initial_oranges = 60
    eaten_oranges = 10
    remaining_oranges = initial_oranges - eaten_oranges
    stolen_oranges = remaining_oranges / 2
    returned_oranges = 5
    total_oranges = remaining_oranges - stolen_oranges + returned_oranges
    result = total_oranges
    return result

print(solution())