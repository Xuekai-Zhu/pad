def solution():
    """Randy just turned 12 and started playing the piano. His friend Sheila told him about the 10,000-hour rule which says, after 10,000 hours of practice, you become an expert or master in your field. If Randy wants to become a piano expert before he is 20, how many hours a day will he need to practice if he practices every day, Monday – Friday, and takes two weeks off for vacation each year?"""
    # Define the total number of years Randy has to become an expert
    total_years = 8

    # Define the number of weeks Randy takes off every year
    off_weeks_per_year = 2

    # Define the number of days Randy practices per week
    practice_days_per_week = 5

    # Define the total number of practice days in a year
    practice_days_per_year = (365 - (off_weeks_per_year * 14)) * practice_days_per_week / 7

    # Calculate the total number of practice hours Randy needs to become an expert
    total_practice_hours = 10000

    # Calculate the number of practice hours Randy needs per day
    practice_hours_per_day = total_practice_hours / (total_years * practice_days_per_year)

    # Return the result
    result = practice_hours_per_day
    return result

print(solution())