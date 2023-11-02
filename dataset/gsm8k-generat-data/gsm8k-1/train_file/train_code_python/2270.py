def solution():
    """Last year, Peter organized a Fun Run for his community project and 200 people signed up. Forty people did not show up to run.
    This year, there will be twice as many runners as last year. How many people will run this year?"""
    last_year_runners = 200
    no_show = 40
    this_year_runners = (last_year_runners - no_show) * 2
    result = this_year_runners
    return result

print(solution())