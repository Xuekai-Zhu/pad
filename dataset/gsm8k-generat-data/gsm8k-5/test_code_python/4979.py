def solution():
    # Calculate the total number of hours Annie spends on extracurriculars per week
    total_hours_per_week = 2 + 8 + 3  # 2 hours on chess club, 8 hours on drama club, and 3 hours on glee club

    # Calculate the number of weeks between the start of the semester and midterms
    weeks_to_midterms = 12 / 2 - 2  # There are 12 weeks in a semester, and Annie takes the first two weeks off sick

    # Calculate the total number of hours Annie spends on extracurriculars before midterms
    total_hours_before_midterms = total_hours_per_week * weeks_to_midterms
    result = total_hours_before_midterms
    return result

print(solution())