def solution():
    # Define the study time for each chapter and worksheet
    chapter_time = 3
    worksheet_time = 1.5

    # Calculate the total study time for both chapters and worksheets
    total_time = (chapter_time * 2) + (worksheet_time * 4)

    # Calculate the total break time in minutes
    total_break_time = (10 + (3 * 10)) * 7 + (30 * 7)

    # Convert the total break time to hours
    total_break_time_hours = total_break_time / 60

    # Calculate the total time including breaks
    total_time_including_breaks = total_time + total_break_time_hours

    # Calculate the number of days required to study for no more than 4 hours each day
    days_to_study = total_time_including_breaks / 4
    result = days_to_study
    return result

print(solution())