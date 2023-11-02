def solution():
    
    carrying_capacity = 80
    first_pickup = 3 / 5 * carrying_capacity
    current_capacity = first_pickup + 50
    people_left_behind = max(0, current_capacity - carrying_capacity)
    result = people_left_behind
    return result

print(solution())