def solution():
    """There are 15 students in the art club. By the end of each quarter, each student makes two artworks. If there are four quarters in a school year, how many artworks can the art club collect in two school years?"""
    num_students = 15
    artworks_per_student = 2
    quarters_per_year = 4
    years = 2
    total_artworks = num_students * artworks_per_student * quarters_per_year * years
    result = total_artworks
    return result

print(solution())