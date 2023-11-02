def solution():
    """Annie brought 20 brownies to school.  She gave half of them to the school administrator to put in the faculty lounge.  Of the remaining brownies, she gave half to her best friend, Carl, and another two to her friend, Simon.  How many brownies did she have left?"""
    # Define the initial number of brownies
    initial_brownies = 20

    # Calculate the number of brownies given to the school administrator
    admin_brownies = initial_brownies // 2

    # Calculate the remaining number of brownies
    remaining_brownies = initial_brownies - admin_brownies

    # Calculate the number of brownies given to Carl
    carl_brownies = remaining_brownies // 2

    # Calculate the final number of brownies
    final_brownies = carl_brownies - 2

    # Display the final number of brownies
    result = final_brownies
    return result

print(solution())