def solution():
    # Calculate the number of towels each person can fold in one minute
    jane_towels_per_minute = 3/5
    kyla_towels_per_minute = 5/10
    anthony_towels_per_minute = 7/20

    # Calculate the total number of towels they can fold together in one minute
    total_towels_per_minute = jane_towels_per_minute + kyla_towels_per_minute + anthony_towels_per_minute

    # Calculate the total number of towels they can fold together in one hour
    total_towels_per_hour = total_towels_per_minute * 60

    result = total_towels_per_hour
    return result

print(solution())