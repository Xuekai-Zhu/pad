def solution():
    # Calculate the total marks scored by the first 10 students
    marks_first_10 = 10 * 90

    # Find the total marks scored by the next 15 students
    marks_next_15 = 15 * (90 - 10)

    # Find the total marks of the remaining students
    marks_remaining = (50 - 10 - 15) * 60

    # Find the total marks scored by the whole class
    total_marks = marks_first_10 + marks_next_15 + marks_remaining

    # Find the average marks for the whole class
    avg_marks = total_marks / 50
    result = avg_marks
    return result

print(solution())