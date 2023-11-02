def solution():
    
    textbook_chapters = 2
    worksheet_sets = 4
    textbook_hours = 3
    worksheet_hours = 1.5
    max_study_hours_per_day = 4 - (10 + 10 + 10 + 30) / 60  
    total_textbook_hours = textbook_chapters * textbook_hours
    total_worksheet_hours = worksheet_sets * worksheet_hours
    total_study_hours_per_day = total_textbook_hours + total_worksheet_hours
    days_needed = (total_textbook_hours + total_worksheet_hours) / max_study_hours_per_day

    result = days_needed
    return result

print(solution())