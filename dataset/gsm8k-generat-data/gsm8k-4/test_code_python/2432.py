def solution():
    """Annie brought 20 brownies to school. She gave half of them to the school administrator to put in the faculty lounge. Of the remaining brownies, she gave half to her best friend, Carl, and another two to her friend, Simon. How many brownies did she have left?"""
    # Define the initial number of brownies
    brownies = 20

    # Calculate the number of brownies given to the school administrator
    brownies_admin = brownies / 2

    # Calculate the number of brownies remaining
    brownies_remaining = brownies - brownies_admin

    # Calculate the number of brownies given to Carl
    brownies_carl = brownies_remaining / 2

    # Calculate the number of brownies remaining
    brownies_remaining = brownies_remaining - brownies_carl - 2

    result = brownies_remaining
    return result

print(solution())