def solution():
    
    students = 15
    artworks_per_student = 2
    quarters_per_year = 4
    artworks_per_year = students * artworks_per_student * quarters_per_year
    artworks_in_two_years = artworks_per_year * 2
    result = artworks_in_two_years
    return result

print(solution())