def solution():
    """There are 20 students in the orchestra and twice that number in the band. There are 12 boys and 16 girls in the choir. If each student only participates in one group, how many students, in total, are there in the orchestra, the band, and the choir?"""
    orchestra_students = 20
    band_students = 2 * orchestra_students
    choir_students = 12 + 16
    total_students = orchestra_students + band_students + choir_students
    result = total_students
    return result

print(solution())