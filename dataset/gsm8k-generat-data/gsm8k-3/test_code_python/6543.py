def solution():
    """On the planet Orbius-5, there are 250 days per year, and each year is equally divided into 5 seasons. If an astronaut from earth lands on planet Orbius-5 and stays there for 3 seasons before returning to earth, what is the number of days the astronaut will spend on Orbius-5?"""
    # Define the number of days in a year and the number of seasons in a year
    DAYS_PER_YEAR = 250
    SEASONS_PER_YEAR = 5

    # Calculate the number of days in a season
    days_per_season = DAYS_PER_YEAR // SEASONS_PER_YEAR

    # Calculate the number of days spent on Orbius-5
    days_on_Orbius5 = days_per_season * 3

    # Display the number of days spent on Orbius-5
    result = days_on_Orbius5
    return result

print(solution())