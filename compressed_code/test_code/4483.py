def solution():
    
    initial_beavers = 20
    initial_chipmunks = 40
    final_beavers = 2 * initial_beavers
    final_chipmunks = initial_chipmunks - 10
    total_animals = initial_beavers + initial_chipmunks + final_beavers + final_chipmunks
    result = total_animals
    return result

print(solution())