def solution():
    
    initial_feathers = 5263
    cars_dodged = 23
    feathers_pulled = 2 * cars_dodged
    remaining_feathers = initial_feathers - feathers_pulled
    total_feathers = remaining_feathers
    return total_feathers

print(solution())