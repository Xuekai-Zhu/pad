def solution():
    weeks_per_year = 52  # There are 52 weeks in a year
    wash_frequency = 4  # Helen washes her silk pillowcases every 4 weeks
    total_washes = weeks_per_year // wash_frequency  # Helen hand washes her pillowcases this many times in a year

    time_per_wash = 0.5  # It takes Helen 30 minutes to hand wash all of her silk pillowcases
    total_time = total_washes * time_per_wash  # Helen spends this much time in total hand washing her pillowcases

    result = total_time
    return result

print(solution())