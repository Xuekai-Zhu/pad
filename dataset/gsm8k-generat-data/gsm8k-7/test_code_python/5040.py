def solution():
    num_ducks = 320

    # Calculate the number of ducks left after the fox eats 1/4 of them
    num_ducks -= num_ducks / 4

    # Calculate the number of ducks left after 1/6 of them fly away
    num_ducks -= num_ducks / 6

    # Calculate the number of ducks left after 30% of them are stolen
    num_ducks -= num_ducks * 0.3

    result = num_ducks
    return result

print(solution())