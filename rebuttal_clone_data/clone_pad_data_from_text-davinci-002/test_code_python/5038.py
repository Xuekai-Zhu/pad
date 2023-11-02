def solution():
    initial_peanuts = 148
    peanuts_eaten = initial_peanuts / 4 + 29
    peanuts_left = initial_peanuts - peanuts_eaten
    result = peanuts_left
    return result

print(solution())