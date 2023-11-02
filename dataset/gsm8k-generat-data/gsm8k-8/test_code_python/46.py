def solution():
    # Calculate the total minutes practicing piano per week
    piano_time_per_day = 20
    piano_time_per_week = piano_time_per_day * 6

    # Calculate the total minutes practicing violin per week
    violin_time_per_week = piano_time_per_week * 3

    # Calculate the total minutes practicing per week
    total_time_per_week = piano_time_per_week + violin_time_per_week

    # Calculate the total minutes practicing per month
    total_time_per_month = total_time_per_week * 4

    result = total_time_per_month
    return result

print(solution())