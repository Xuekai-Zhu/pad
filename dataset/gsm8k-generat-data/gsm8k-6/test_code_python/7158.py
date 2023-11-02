def solution():
    # Calculate the total number of artworks the art club can collect in two school years
    total_students = 15
    artworks_per_student_per_quarter = 2
    quarters_per_school_year = 4
    years = 2
    total_artworks = total_students * artworks_per_student_per_quarter * quarters_per_school_year * years
    result = total_artworks
    return result

print(solution())