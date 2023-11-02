def solution():
    sandwiches_made = 12
    sandwiches_eaten = (sandwiches_made / 2) + 2
    sandwiches_left = sandwiches_made - sandwiches_eaten
    result = sandwiches_left
    return result

print(solution())