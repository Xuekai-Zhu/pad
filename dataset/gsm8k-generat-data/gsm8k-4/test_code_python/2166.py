def solution():
    """A wheel on a certain machine makes 6 turns every 30 seconds. How many turns does it make in two hours?"""
    # Define the number of turns made in 30 seconds
    turns_per_30_seconds = 6

    # Calculate the number of turns made in one second
    turns_per_second = turns_per_30_seconds / 30

    # Calculate the number of turns made in one minute
    turns_per_minute = turns_per_second * 60

    # Calculate the number of turns made in one hour
    turns_per_hour = turns_per_minute * 60

    # Calculate the number of turns made in two hours
    turns_in_two_hours = turns_per_hour * 2

    result = turns_in_two_hours
    return result

print(solution())