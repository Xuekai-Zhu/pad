def solution():
    initial_sandwiches = 20
    sandwiches_kept = initial_sandwiches / 2
    sandwiches_given = 4
    sandwiches_left = initial_sandwiches - sandwiches_kept - sandwiches_given
    result = sandwiches_left
    return result

print(solution())