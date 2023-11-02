def solution():
    time_dog = 2.5 * 60  # convert grooming time for dog to minutes
    time_cat = 0.5 * 60  # convert grooming time for cat to minutes
    total_time = 5 * time_dog + 3 * time_cat  # multiply grooming time for each animal by number of animals
    result = total_time
    return result

print(solution())