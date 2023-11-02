def solution():
    """The number of math problems that Marvin practiced today is three times as many as the number of problems he solved yesterday. His friend, Arvin, has practiced twice as many math problems on each day. How many math problems have they practiced altogether if Marvin solved 40 math problems yesterday?"""
    # Marvin's number of problems solved today is three times that of yesterday's
    marvin_today = 3 * 40

    # Marvin's total number of problems solved is yesterday's plus today's
    marvin_total = marvin_today + 40

    # Arvin practiced twice as many problems as Marvin each day
    arvin_daily = 2 * (40 + marvin_today)

    # Total number of problems practiced by both Marvin and Arvin
    total_problems = marvin_total + arvin_daily

    result = total_problems
    return result

print(solution())