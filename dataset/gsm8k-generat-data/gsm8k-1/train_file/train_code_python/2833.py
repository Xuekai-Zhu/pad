def solution():
    """The number of math problems that Marvin practiced today is three times as many as the number of problems he solved yesterday. His friend, Arvin, has practiced twice as many math problems on each day. How many math problems have they practiced altogether if Marvin solved 40 math problems yesterday?"""
    marvin_yesterday = 40
    marvin_today = marvin_yesterday * 3
    arvin = marvin_yesterday * 2
    total_problems = marvin_yesterday + marvin_today + arvin
    result = total_problems
    return result

print(solution())