def solution():
    """Last year, Peter organized a Fun Run for his community project and 200 people signed up. Forty people did not show up to run. This year, there will be twice as many runners as last year. How many people will run this year?"""
    # Define the number of runners last year
    runners_last_year = 200 - 40

    # Define the number of runners this year
    runners_this_year = runners_last_year * 2

    # return the result
    result = runners_this_year
    return result

print(solution())