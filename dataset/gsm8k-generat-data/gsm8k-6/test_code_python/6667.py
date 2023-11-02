def solution():
    # Calculate the total time Rachel spent on the essay in minutes
    total_minutes = 45 + 6*30 + 75  # 45 minutes researching, 6 pages at 30 minutes per page, 75 minutes editing
    # Convert total minutes to hours
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())