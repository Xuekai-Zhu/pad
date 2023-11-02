def solution():
    """Randy just turned 12 and started playing the piano. His friend Sheila told him about the 10,000-hour rule which says, after 10,000 hours of practice, you become an expert or master in your field. If Randy wants to become a piano expert before he is 20, how many hours a day will he need to practice if he practices every day, Monday – Friday, and takes two weeks off for vacation each year?"""
    total_weeks = (20 - 12) * 52 # Number of weeks between ages 12 and 20
    total_days = total_weeks * 5 # Number of weekdays during that time
    total_vacation_weeks = 2 * 8 # Two weeks off each year for eight years
    total_practice_days = total_days - total_vacation_weeks * 5 # Subtracting vacation days
    hours_per_day = 10000 / total_practice_days # Hours needed to practice per day
    result = hours_per_day
    return result

print(solution())