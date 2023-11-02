def solution():
    """A wheel on a certain machine makes 6 turns every 30 seconds. How many turns does it make in two hours?"""
    # Define the number of turns per second
    TURNS_PER_SECOND = 6/30

    # Define the number of seconds in two hours
    SECONDS_IN_TWO_HOURS = 2 * 60 * 60

    # Calculate the total number of turns
    total_turns = TURNS_PER_SECOND * SECONDS_IN_TWO_HOURS

    # Display the total number of turns
    result = total_turns
    return result

print(solution())