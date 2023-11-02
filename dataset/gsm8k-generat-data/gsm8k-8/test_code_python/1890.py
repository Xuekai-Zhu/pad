def solution():
    # Calculate how many towels each person can fold in one minute
    jane_towels_per_min = 3/5
    kyla_towels_per_min = 5/10
    anthony_towels_per_min = 7/20

    # Calculate how many towels they can fold together in one minute
    total_towels_per_min = jane_towels_per_min + kyla_towels_per_min + anthony_towels_per_min

    # Calculate how many towels they can fold in one hour
    towels_per_hour = total_towels_per_min * 60

    result = towels_per_hour
    return result

print(solution())