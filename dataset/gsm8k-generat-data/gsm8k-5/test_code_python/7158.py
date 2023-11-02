def solution():
    students = 15  # There are 15 students in the art club
    artworks_per_student = 2  # Each student makes 2 artworks by the end of each quarter
    quarters_per_year = 4  # There are 4 quarters in a year
    years = 2  # The question asks for the number of artworks in 2 years

    # Calculate the total number of artworks made by the art club in one year
    artworks_per_year = students * artworks_per_student * quarters_per_year

    # Calculate the total number of artworks made by the art club in two years
    artworks_total = artworks_per_year * years
    result = artworks_total
    return result

print(solution())