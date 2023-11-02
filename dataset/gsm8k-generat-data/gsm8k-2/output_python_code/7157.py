def solution():
    """There are 15 students in the art club. By the end of each quarter, each student makes two artworks. If there are four quarters in a school year, how many artworks can the art club collect in two school years?"""
    students = 15
    artworks_per_student = 2
    quarters_per_year = 4
    artworks_per_year = students * artworks_per_student * quarters_per_year
    artworks_in_two_years = artworks_per_year * 2
    result = artworks_in_two_years
    return result

print(solution())