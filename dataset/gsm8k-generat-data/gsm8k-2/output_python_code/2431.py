def solution():
    """Annie brought 20 brownies to school. She gave half of them to the school administrator to put in the faculty lounge. Of the remaining brownies, she gave half to her best friend, Carl, and another two to her friend, Simon. How many brownies did she have left?"""
    total_brownies = 20
    lounge_brownies = total_brownies // 2
    remaining_brownies = total_brownies - lounge_brownies
    carl_brownies = remaining_brownies // 2
    simon_brownies = 2
    left_brownies = remaining_brownies - carl_brownies - simon_brownies
    result = left_brownies
    return result

print(solution())