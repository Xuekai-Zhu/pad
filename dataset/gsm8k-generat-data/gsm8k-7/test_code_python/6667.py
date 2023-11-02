def solution():
    pages_written = 6
    time_per_page = 30  # in minutes
    research_time = 45  # in minutes
    editing_time = 75  # in minutes

    # Calculate the total time spent writing
    writing_time = pages_written * time_per_page

    # Calculate the total time spent completing the essay
    total_time = research_time + writing_time + editing_time

    # Convert the total time into hours
    hours_spent = total_time / 60
    result = hours_spent
    return result

print(solution())