def solution():
    # Convert time to minutes
    jane_time = 5
    kyla_time = 10
    anthony_time = 20

    # Calculate the number of towels each person can fold per minute
    jane_rate = 3 / jane_time
    kyla_rate = 5 / kyla_time
    anthony_rate = 7 / anthony_time

    # Calculate the combined rate of all three people
    combined_rate = jane_rate + kyla_rate + anthony_rate

    # Calculate the total number of towels they can fold in one hour (60 minutes)
    total_towels = combined_rate * 60

    result = total_towels
    return result

print(solution())