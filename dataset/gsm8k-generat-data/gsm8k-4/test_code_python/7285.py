def solution():
    """There are 20 students in the orchestra and twice that number in the band. There are 12 boys and 16 girls in the choir. If each student only participates in one group, how many students, in total, are there in the orchestra, the band, and the choir?"""
    # Define the number of students in the orchestra
    orchestra_students = 20

    # Define the number of students in the band
    band_students = orchestra_students * 2

    # Define the number of students in the choir
    choir_students = 12 + 16

    # Calculate the total number of students
    total_students = orchestra_students + band_students + choir_students

    # Return the result
    result = total_students
    return result

print(solution())