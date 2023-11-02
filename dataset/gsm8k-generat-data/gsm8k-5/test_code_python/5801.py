def solution():
    beavers_first_time = 20
    chipmunks_first_time = 40
    beavers_second_time = beavers_first_time * 2
    chipmunks_second_time = chipmunks_first_time - 10
    total_animals = beavers_first_time + chipmunks_first_time + beavers_second_time + chipmunks_second_time
    result = total_animals
    return result

print(solution())