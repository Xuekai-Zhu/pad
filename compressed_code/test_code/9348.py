def solution():
    
    initial_oranges = 60
    eaten_oranges = 10
    remaining_oranges = initial_oranges - eaten_oranges
    stolen_oranges = remaining_oranges / 2
    returned_oranges = 5
    final_oranges = remaining_oranges - stolen_oranges + returned_oranges
    result = final_oranges
    return result

print(solution())