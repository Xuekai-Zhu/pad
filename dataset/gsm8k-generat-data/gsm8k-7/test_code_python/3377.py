def solution():
    practice_time = 120  # 2 hours = 120 minutes

    # Calculate the time spent shooting
    shooting_time = practice_time / 2

    # Calculate the total time spent running and weight lifting
    rw_time = practice_time - shooting_time

    # Calculate the time spent weight lifting using the fact that running takes twice as long as weight lifting
    weightlifting_time = rw_time / 3

    # Convert the time spent weight lifting to minutes
    weightlifting_time_minutes = weightlifting_time * 60
    result = weightlifting_time_minutes
    return result

print(solution())