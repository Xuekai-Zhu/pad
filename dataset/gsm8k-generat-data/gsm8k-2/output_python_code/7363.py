def solution():
    """Angelo and Melanie want to plan how many hours over the next week they should study together for their test next week. They have 2 chapters of their textbook to study and 4 worksheets to memorize. They figure out that they should dedicate 3 hours to each chapter of their textbook and 1.5 hours for each worksheet. If they plan to study no more than 4 hours each day, how many days should they plan to study total over the next week if they take a 10-minute break every hour, include 3 10-minute snack breaks each day, and 30 minutes for lunch each day?"""
    textbook_chapters = 2
    worksheet_sets = 4
    textbook_hours = 3
    worksheet_hours = 1.5
    max_study_hours_per_day = 4 - (10 + 10 + 10 + 30) / 60  # subtracting break times from max study hours per day
    total_textbook_hours = textbook_chapters * textbook_hours
    total_worksheet_hours = worksheet_sets * worksheet_hours
    total_study_hours_per_day = total_textbook_hours + total_worksheet_hours
    days_needed = (total_textbook_hours + total_worksheet_hours) / max_study_hours_per_day

    result = days_needed
    return result

print(solution())