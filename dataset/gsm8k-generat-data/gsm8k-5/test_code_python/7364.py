def solution():
    num_chapters = 2  # Angelo and Melanie have 2 chapters to study
    num_worksheets = 4  # Angelo and Melanie have 4 worksheets to memorize
    study_hours_textbook = 3  # Angelo and Melanie need 3 hours to study each chapter
    study_hours_worksheet = 1.5  # Angelo and Melanie need 1.5 hours to study each worksheet
    max_study_hours_per_day = 4  # Angelo and Melanie can study no more than 4 hours each day
    total_break_time = (10 * 4) + (10 * 3) + 30  # Total break time (10-minute break every hour, 3 snack breaks, and 30-minute lunch break)

    # Calculate the total study time required
    total_study_time = (num_chapters * study_hours_textbook) + (num_worksheets * study_hours_worksheet)

    # Calculate the total number of days required to study
    total_study_days = (total_study_time / max_study_hours_per_day) + 1  # Add an extra day for leftover hours
    total_study_days = int(total_study_days)  # Convert to integer type

    # Calculate the total time required (including breaks)
    total_time_hours = (total_study_days * max_study_hours_per_day) + (total_break_time / 60)
    total_time_minutes = int((total_time_hours - int(total_time_hours)) * 60)
    total_time_hours = int(total_time_hours)

    result = total_study_days
    return result

print(solution())