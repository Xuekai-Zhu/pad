def solution():
    """There are 20 students in the orchestra and twice that number in the band. There are 12 boys and 16 girls in the choir. If each student only participates in one group, how many students, in total, are there in the orchestra, the band, and the choir?"""
    orchestra_count = 20
    band_count = 2 * orchestra_count
    choir_count = 12 + 16
    total_students = orchestra_count + band_count + choir_count
    result = total_students
    return result

print(solution())