def solution():
    # Calculate the total number of pills Jeremy takes in 2 weeks
    pills_per_day = 1000/500  # Jeremy takes 1000 mg every 6 hours, which is equivalent to 2 pills of 500 mg every 6 hours
    pills_per_week = pills_per_day * 4 * 7  # Jeremy takes pills 4 times a day for 7 days in a week
    total_pills = pills_per_week * 2  # Jeremy takes pills for 2 weeks
    result = int(total_pills)
    return result

print(solution())