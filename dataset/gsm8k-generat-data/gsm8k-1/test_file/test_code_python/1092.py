def solution():
    """Billy is volunteering his time to help people do their taxes. He can help 2 people per hour for 3 hours a day. 
    If he takes 20% of the days between March 1st and April 19th off, and helps people on all the other days.
    How many people does he help? (Remember there are 31 days in March.)"""
    people_per_hour = 2
    hours_per_day = 3
    days_worked = 31 + 19  # March + April 1-19
    days_off = int(days_worked * 0.2)
    days_helping = days_worked - days_off
    total_hours = days_helping * hours_per_day
    total_people = total_hours * people_per_hour
    result = total_people
    return result

print(solution())