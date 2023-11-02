def solution():
    # Calculate the number of ducks remaining after the first night
    ducks_remaining = 320 * (3/4)

    # Calculate the number of ducks remaining after the second night
    ducks_remaining = ducks_remaining * (5/6)

    # Calculate the number of ducks remaining after the third night
    ducks_remaining = ducks_remaining * (0.7)

    result = ducks_remaining
    return result

print(solution())