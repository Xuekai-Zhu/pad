def solution():
    total_land = 20000
    num_siblings = 4

    # Divide the total land equally among all siblings
    land_per_person = total_land / (num_siblings + 1)

    # Calculate how much land Jose will have
    jose_land = land_per_person

    result = jose_land
    return result

print(solution())