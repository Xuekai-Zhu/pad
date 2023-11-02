def solution():
    # Calculate Mario's salary from last year
    mario_last_year = 4000 / 1.4

    # Calculate Bob's salary from last year
    bob_last_year = 3 * mario_last_year

    # Calculate Bob's current salary
    bob_current = bob_last_year * 1.2

    result = bob_current
    return result

print(solution())