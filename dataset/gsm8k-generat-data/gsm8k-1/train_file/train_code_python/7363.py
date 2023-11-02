def solution():
    """Angelo and Melanie want to plan how many hours over the next week they should study together for their test next week. They have 2 chapters of their textbook to study and 4 worksheets to memorize. They figure out that they should dedicate 3 hours to each chapter of their textbook and 1.5 hours for each worksheet. If they plan to study no more than 4 hours each day, how many days should they plan to study total over the next week if they take a 10-minute break every hour, include 3 10-minute snack breaks each day, and 30 minutes for lunch each day?"""
    
    # Calculate total study time needed
    hours_per_chapter = 3
    hours_per_worksheet = 1.5
    chapters_to_study = 2
    worksheets_to_memorize = 4
    total_study_time = (hours_per_chapter * chapters_to_study) + (hours_per_worksheet * worksheets_to_memorize)
    
    # Calculate total break time per day
    breaks_per_day = 4  # 10-minute breaks for every hour studied
    snack_breaks_per_day = 3
    total_break_time_per_day = (breaks_per_day + snack_breaks_per_day) * 10
    
    # Calculate total study time per day, including break time
    total_study_time_per_day = 4 * 60 - total_break_time_per_day - 30  # 30 minutes for lunch
    
    # Calculate total days needed to study
    total_days = total_study_time / total_study_time_per_day
    
    result = total_days
    return result

print(solution())