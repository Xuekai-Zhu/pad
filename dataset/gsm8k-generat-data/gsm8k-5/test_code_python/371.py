def solution():
    burgers_per_session = 15  # Ronald can grill 15 hamburgers per session
    total_burgers = 115  # Ronald needs to cook 115 hamburgers in total
    burgers_cooked = 40  # Ronald has already cooked 40 hamburgers

    # Calculate the number of remaining hamburgers to be cooked
    remaining_burgers = total_burgers - burgers_cooked

    # Calculate the number of sessions needed to cook the remaining hamburgers
    sessions_needed = remaining_burgers / burgers_per_session
    result = sessions_needed
    return result

print(solution())