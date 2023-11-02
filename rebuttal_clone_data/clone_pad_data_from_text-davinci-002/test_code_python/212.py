def solution():
     """Randy just turned 12 and started playing the piano. His friend Sheila told him about the 10,000-hour rule which says, after 10,000 hours of practice, you become an expert or master in your field. If Randy wants to become a piano expert before he is 20, how many hours a day will he need to practice if he practices every day, Monday – Friday, and takes two weeks off for vacation each year?"""
     hours_needed = 10000
     days_in_a_year = 365
     days_in_a_week = 7
     hours_in_a_day = 24
     months_in_a_year = 12
     weeks_in_a_year = 52
     hours_in_a_week = hours_in_a_day * days_in_a_week
     hours_in_a_year = hours_in_a_week * weeks_in_a_year
     years_needed = hours_needed / hours_in_a_year
     hours_per_day = hours_needed / (days_in_a_year * years_needed)
     result = hours

print(solution())