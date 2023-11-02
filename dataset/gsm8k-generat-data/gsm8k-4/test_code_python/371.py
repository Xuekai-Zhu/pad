def solution():
    """Ronald can grill 15 hamburgers per session on his new grill. He needs to cook 115 hamburgers in total for tonight's party. He has already cooked 40 hamburgers. How many more sessions will it take Ronald to finish cooking all 115 hamburgers?"""
    # Define the number of hamburgers that Ronald can grill in one session
    hamburgers_per_session = 15

    # Define the total number of hamburgers that Ronald needs to cook
    total_hamburgers = 115

    # Define the number of hamburgers already cooked
    hamburgers_cooked = 40

    # Calculate the remaining number of hamburgers to cook
    hamburgers_remaining = total_hamburgers - hamburgers_cooked

    # Calculate the number of sessions required to cook the remaining hamburgers
    sessions_required = hamburgers_remaining / hamburgers_per_session

    # Round up the number of sessions required
    sessions_required = int(math.ceil(sessions_required))

    # return the result
    result = sessions_required
    return result

print(solution())