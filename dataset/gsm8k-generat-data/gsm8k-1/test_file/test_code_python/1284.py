def solution():
    """Every day Charisma meditates for 15 minutes when she first wakes up and again before she goes to sleep. 5 days a week she practices 1 hour of yoga. in 4 weeks, how much time has she spent on meditation/yoga practice?"""
    meditation_per_day = 30 # 15 minutes in the morning and 15 minutes at night
    yoga_per_week = 5 * 60 # 1 hour of yoga per day for 5 days
    total_time = (meditation_per_day * 7 * 4) + yoga_per_week * 4 # multiply time per day/week by number of days/weeks
    result = total_time
    return result

print(solution())