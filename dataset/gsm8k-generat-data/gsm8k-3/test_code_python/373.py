def solution():
    """Ronald can grill 15 hamburgers per session on his new grill.  He needs to cook 115 hamburgers in total for tonight's party.  He has already cooked 40 hamburgers.  How many more sessions will it take Ronald to finish cooking all 115 hamburgers?"""
    # Define the number of hamburgers Ronald can grill per session
    HAMBURGERS_PER_SESSION = 15

    # Define the number of hamburgers Ronald has already cooked
    hamburgers_cooked = 40

    # Define the number of hamburgers Ronald needs to grill in total
    total_hamburgers = 115

    # Calculate the number of hamburgers Ronald still needs to cook
    hamburgers_left = total_hamburgers - hamburgers_cooked

    # Calculate the number of sessions Ronald still needs to grill
    sessions_left = hamburgers_left // HAMBURGERS_PER_SESSION
    if hamburgers_left % HAMBURGERS_PER_SESSION != 0:
        sessions_left += 1

    # Display the number of sessions Ronald still needs to grill
    result = sessions_left
    return result

print(solution())