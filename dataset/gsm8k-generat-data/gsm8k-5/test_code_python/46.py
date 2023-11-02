def solution():
    piano_time = 20  # Carolyn practices the piano for 20 minutes a day
    violin_time = 3 * piano_time  # Carolyn practices the violin for three times as long
    days_per_week = 6  # Carolyn practices six days a week
    weeks_per_month = 4  # Carolyn wants to know how many minutes she practices in a month with four weeks

    # Calculate the total time Carolyn spends practicing each day
    total_time_per_day = piano_time + violin_time

    # Calculate the total time Carolyn spends practicing each week
    total_time_per_week = total_time_per_day * days_per_week

    # Calculate the total time Carolyn spends practicing in a month
    total_time_per_month = total_time_per_week * weeks_per_month
    result = total_time_per_month
    return result

print(solution())