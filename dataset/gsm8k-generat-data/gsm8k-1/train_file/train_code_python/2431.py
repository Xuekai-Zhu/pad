def solution():
    """Annie brought 20 brownies to school. She gave half of them to the school administrator to put in the faculty lounge. Of the remaining brownies, she gave half to her best friend, Carl, and another two to her friend, Simon. How many brownies did she have left?"""
    total_brownies = 20
    admin_brownies = total_brownies / 2
    remaining_brownies = total_brownies - admin_brownies
    carl_brownies = remaining_brownies / 2
    remaining_brownies = remaining_brownies - carl_brownies - 2
    result = remaining_brownies
    return result

print(solution())