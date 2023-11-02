def solution():
    # Calculate the total time spent walking dogs on Monday and Wednesday
    time_poodles = 4 * 2  # 4 poodles, each taking 2 hours
    time_chihuahuas = 2 * 1  # 2 Chihuahuas, each taking 1 hour
    time_labradors = 4 * 3  # 4 Labradors, each taking 3 hours
    time_monday_wednesday = time_poodles + time_chihuahuas + time_labradors

    # Calculate the total time available for dog-walking on Tuesday
    time_tuesday = 32 - time_monday_wednesday

    # Calculate how many poodles Charlotte can walk on Tuesday
    time_per_poodle = 2  # Each poodle takes 2 hours to walk
    poodles_tuesday = time_tuesday // time_per_poodle

    result = poodles_tuesday
    return result

print(solution())