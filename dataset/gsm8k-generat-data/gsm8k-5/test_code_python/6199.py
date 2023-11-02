def solution():
    # Let's represent the number of floors in Building B by x
    # Then, the number of floors in Building A is x - 9
    # And the number of floors in Building C is 5x - 6

    # We are given that Building A has 4 floors, so we can write:
    x - 9 = 4
    # Solving for x:
    x = 13

    # Now we can find the number of floors in Building C:
    5x - 6 = 5(13) - 6
    floors_c = 59

    result = floors_c
    return result

print(solution())