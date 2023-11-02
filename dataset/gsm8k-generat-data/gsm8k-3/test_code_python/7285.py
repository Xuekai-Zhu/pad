def solution():
    """There are 20 students in the orchestra and twice that number in the band. There are 12 boys and 16 girls in the choir. If each student only participates in one group, how many students, in total, are there in the orchestra, the band, and the choir?"""
    # Calculate the number of students in the band
    band_students = 20 * 2

    # Calculate the total number of students
    total_students = 20 + band_students + 12 + 16

    # Display the total number of students
    result = total_students
    return result

print(solution())