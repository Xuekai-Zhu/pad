def solution():
    # Calculate the total number of spiral shells
    total_shells = 45 * 3

    # Calculate the total number of starfish
    total_starfish = total_shells * 2

    # Calculate the total number of souvenirs
    total_souvenirs = 45 + total_shells + total_starfish
    result = total_souvenirs
    return result

print(solution())