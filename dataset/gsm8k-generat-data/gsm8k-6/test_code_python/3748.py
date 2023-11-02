def solution():
    # Calculate the number of aquariums Lucy can clean in 24 hours of work
    # Lucy can clean 2 aquariums in 3 hours, so she can clean (2/3) aquariums in 1 hour
    aquariums_per_hour = 2/3
    total_aquariums = aquariums_per_hour * 24
    result = total_aquariums
    return result

print(solution())