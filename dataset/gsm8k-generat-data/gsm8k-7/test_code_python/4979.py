def solution():
    chess_hours = 2
    drama_hours = 8
    glee_hours = 3
    num_weeks = 12
    weeks_off = 2

    # Calculate the total number of weeks Annie attends extracurriculars
    total_weeks = num_weeks - weeks_off

    # Calculate the total number of hours Annie spends on extracurriculars before midterms
    total_hours = (chess_hours + drama_hours + glee_hours) * total_weeks

    result = total_hours
    return result

print(solution())