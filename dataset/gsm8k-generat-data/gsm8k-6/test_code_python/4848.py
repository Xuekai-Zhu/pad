def solution():
    # Calculate the number of men with college degrees
    men_with_degrees = (25/100) * (total_employees - (total_employees * (60/100)))  # 60% of employees are women, so the remaining 40% are men
    men_without_degrees = 8  # Given in the question
    total_men = men_with_degrees + men_without_degrees  # Find the total number of men
    women = total_employees * (60/100)  # Find the number of women
    result = women
    return result

print(solution())