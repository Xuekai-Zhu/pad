def solution():
    # Calculate the number of turns the wheel makes in 1 second
    turns_per_second = 6/30

    # Calculate the number of turns the wheel makes in 1 minute
    turns_per_minute = turns_per_second * 60

    # Calculate the number of turns the wheel makes in 1 hour
    turns_per_hour = turns_per_minute * 60

    # Calculate the number of turns the wheel makes in 2 hours
    turns_in_2_hours = turns_per_hour * 2
    result = turns_in_2_hours
    return result

print(solution())