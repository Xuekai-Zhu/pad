def solution():
    """On the planet Orbius-5, there are 250 days per year, and each year is equally divided into 5 seasons. If an astronaut from earth lands on planet Orbius-5 and stays there for 3 seasons before returning to earth, what is the number of days the astronaut will spend on Orbius-5?"""
    # Define the number of seasons per year and the number of days per season
    NUM_SEASONS_PER_YEAR = 5
    DAYS_PER_SEASON = 250 / NUM_SEASONS_PER_YEAR

    # Calculate the total number of days the astronaut will spend on Orbius-5
    total_days = DAYS_PER_SEASON * 3

    # return the result
    result = total_days
    return result

print(solution())