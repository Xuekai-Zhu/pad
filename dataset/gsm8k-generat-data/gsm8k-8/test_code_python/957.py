def solution():
    # Calculate the total number of coals burned
    total_coals_burned = 3 * 60

    # Calculate the total time in minutes
    total_time_minutes = (20 / 15) * total_coals_burned

    # Convert to hours and minutes
    hours = total_time_minutes // 60
    minutes = total_time_minutes % 60

    # Return the result as a string with "hours" and "minutes" labels
    result = str(int(hours)) + " hours and " + str(int(minutes)) + " minutes"
    return result

print(solution())