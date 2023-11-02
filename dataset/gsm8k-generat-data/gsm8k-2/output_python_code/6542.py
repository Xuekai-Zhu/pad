def solution():
    """On the planet Orbius-5, there are 250 days per year, and each year is equally divided into 5 seasons. If an astronaut from earth lands on planet Orbius-5 and stays there for 3 seasons before returning to earth, what is the number of days the astronaut will spend on Orbius-5?"""
    days_per_season = 250 / 5
    seasons_stayed = 3
    days_spent = days_per_season * seasons_stayed
    result = days_spent
    return result

print(solution())