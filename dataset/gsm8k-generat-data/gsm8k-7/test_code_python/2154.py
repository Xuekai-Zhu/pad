def solution():
    full_capacity = 300 * 4
    initial_carrying_capacity = full_capacity - 100
    initial_num_people = initial_carrying_capacity / (4/3)  # one-third of full capacity
    result = initial_num_people
    return result

print(solution())