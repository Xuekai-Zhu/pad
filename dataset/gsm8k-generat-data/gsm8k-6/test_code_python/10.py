def solution():
    # Find out how many people were on the last ship the monster ate
    last_ship = 847
    for i in range(3):
        last_ship = last_ship / 2

    # Find out how many people were on the first ship the monster ate
    first_ship = last_ship / 2

    result = first_ship
    return result

print(solution())