def solution():
    # Calculate the number of students in the Biology hall
    biology_hall = 2 * 30  # twice as many students in Biology hall as in General Study hall

    # Calculate the combined total number of students in General Study hall and Biology hall
    total_students = 30 + biology_hall

    # Calculate the number of students in Math hall
    math_hall = (3/5) * total_students

    # Calculate the total number of students in all three halls combined
    total = total_students + math_hall

    result = total
    return result

print(solution())