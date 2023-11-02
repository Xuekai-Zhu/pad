def solution():
    """Randy just turned 12 and started playing the piano. His friend Sheila told him about the 10,000-hour rule which says, after 10,000 hours of practice, you become an expert or master in your field. If Randy wants to become a piano expert before he is 20, how many hours a day will he need to practice if he practices every day, Monday – Friday, and takes two weeks off for vacation each year?"""
    years_of_practice = 8
    weeks_of_vacation = 2 * 8
    days_of_practice = (365 * years_of_practice) - weeks_of_vacation
    hours_of_practice = 10000 / days_of_practice
    hours_per_day = hours_of_practice / 5
    result = hours_per_day
    return result

print(solution())