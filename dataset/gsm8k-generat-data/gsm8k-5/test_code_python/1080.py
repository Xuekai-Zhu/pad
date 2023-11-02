def solution():
    total_students = 100  # 100% of the students
    women_percentage = 30  # 30% of the students are women
    women_count = 180  # There are 180 women in the engineering department

    # Calculate the percentage of men in the engineering department
    men_percentage = total_students - women_percentage
    men_count = (men_percentage / 100) * (women_count / (1 - (women_percentage / 100)))

    result = men_count
    return result

print(solution())