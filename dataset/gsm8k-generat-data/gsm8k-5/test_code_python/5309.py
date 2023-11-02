def solution():
    recess_minutes = 15 * 2  # Vivian's students get 2 15-minute recess breaks a day
    lunch_minutes = 30  # Vivian's students get a 30-minute lunch break
    extra_recess_minutes = 20  # Vivian's students get an extra 20-minute recess break
    total_minutes_outside = recess_minutes + lunch_minutes + extra_recess_minutes  # Calculate the total time spent outside

    # Convert the total time spent outside to hours and minutes
    hours = total_minutes_outside // 60
    minutes = total_minutes_outside % 60

    result = f"{hours} hours and {minutes} minutes"
    return result

print(solution())