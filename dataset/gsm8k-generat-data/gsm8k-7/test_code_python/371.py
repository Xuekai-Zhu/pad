def solution():
    burgers_per_session = 15
    total_burgers_needed = 115
    burgers_already_cooked = 40

    # Calculate the remaining number of burgers that need to be cooked
    burgers_left = total_burgers_needed - burgers_already_cooked

    # Calculate the number of sessions needed to cook the remaining burgers
    sessions_needed = (burgers_left + burgers_per_session - 1) // burgers_per_session
    result = sessions_needed
    return result

print(solution())