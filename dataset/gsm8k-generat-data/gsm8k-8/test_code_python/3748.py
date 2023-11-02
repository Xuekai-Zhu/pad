def solution():
    # Calculate how many hours Lucy works in a week
    total_hours = 24

    # Calculate how many aquariums Lucy can clean in one hour
    aquariums_per_hour = 2/3

    # Calculate how many aquariums Lucy can clean in a week
    total_aquariums = aquariums_per_hour * total_hours

    result = total_aquariums
    return result

print(solution())