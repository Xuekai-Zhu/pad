def solution():
    # Calculate the total hours of extracurricular activity before midterms
    total_weeks = 12  # total number of weeks in a semester
    sick_weeks = 2  # number of weeks Annie takes off sick
    active_weeks = total_weeks - sick_weeks  # number of weeks she is active in extracurriculars
    chess_hours = 2 * active_weeks  # hours spent on chess club
    drama_hours = 8 * active_weeks  # hours spent on drama club
    glee_hours = 3 * active_weeks  # hours spent on glee club
    total_hours = chess_hours + drama_hours + glee_hours  # total hours of extracurricular activity
    result = total_hours
    return result

print(solution())