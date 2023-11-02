def solution():
    """Randy just turned 12 and started playing the piano. His friend Sheila told him about the 10,000-hour rule which says, after 10,000 hours of practice, you become an expert or master in your field. If Randy wants to become a piano expert before he is 20, how many hours a day will he need to practice if he practices every day, Monday – Friday, and takes two weeks off for vacation each year?"""
    # Calculate the number of practice days Randy has before he turns 20
    practice_years = 20 - 12
    vacation_days = practice_years * 2 * 5 # two weeks off per year
    practice_days = practice_years * 5 * 52 - vacation_days

    # Calculate the number of hours Randy needs to practice
    hours_needed = 10000 / practice_days

    # Calculate the number of hours Randy needs to practice per day
    hours_per_day = hours_needed / 5

    # Display the number of hours Randy needs to practice per day
    result = hours_per_day
    return result

print(solution())