def solution():
    """The number of math problems that Marvin practiced today is three times as many as the number of problems he solved yesterday. His friend, Arvin, has practiced twice as many math problems on each day. How many math problems have they practiced altogether if Marvin solved 40 math problems yesterday?"""
    marvin_yesterday = 40
    marvin_today = 3 * marvin_yesterday
    arvin_today = 2 * marvin_today
    total_problems = marvin_yesterday + marvin_today + arvin_today
    result = total_problems
    return result

print(solution())