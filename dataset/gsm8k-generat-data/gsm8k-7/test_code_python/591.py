def solution():
    cherries_needed = 3 * 80
    cherries_per_batch = 20
    time_per_batch = 10  # minutes
    cherries_pitted = 0
    time_spent = 0  # minutes

    while cherries_pitted < cherries_needed:
        cherries_pitted += cherries_per_batch
        time_spent += time_per_batch

    time_spent_hours = time_spent / 60  # converting minutes to hours
    result = time_spent_hours
    return result

print(solution())