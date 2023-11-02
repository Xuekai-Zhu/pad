def solution():
    """The number of math problems that Marvin practiced today is three times as many as the number of problems he solved yesterday. His friend, Arvin, has practiced twice as many math problems on each day. How many math problems have they practiced altogether if Marvin solved 40 math problems yesterday?"""
    # Define the number of math problems Marvin solved yesterday
    problems_marvin_yesterday = 40

    # Calculate the number of math problems Marvin solved today
    problems_marvin_today = problems_marvin_yesterday * 3

    # Calculate the total number of math problems Marvin solved
    problems_marvin_total = problems_marvin_yesterday + problems_marvin_today

    # Calculate the number of math problems Arvin solved each day
    problems_arvin_per_day = problems_marvin_yesterday * 2

    # Calculate the total number of math problems Arvin solved
    problems_arvin_total = problems_arvin_per_day * 2

    # Calculate the total number of math problems they practiced altogether
    total_problems = problems_marvin_total + problems_arvin_total

    # Display the total number of math problems
    result = total_problems
    return result

print(solution())