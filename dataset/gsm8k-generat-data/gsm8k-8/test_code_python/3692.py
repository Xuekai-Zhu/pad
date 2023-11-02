def solution():
    # Calculate the total number of males and females
    total_males = 17 + 14 + 15
    total_females = 13 + 18 + 17

    # Determine the number of students who cannot be paired
    unpaired_students = abs(total_males - total_females)

    # If there are an odd number of students, one student will be unpaired
    if (total_males + total_females) % 2 != 0:
        unpaired_students += 1

    result = unpaired_students
    return result

print(solution())