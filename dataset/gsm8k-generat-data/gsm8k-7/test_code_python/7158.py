def solution():
    num_students = 15
    num_artworks_per_student_per_quarter = 2
    num_quarters_per_year = 4
    num_years = 2

    # Calculate the total number of artworks per student per year
    num_artworks_per_student_per_year = num_artworks_per_student_per_quarter * num_quarters_per_year

    # Calculate the total number of artworks per student in two years
    num_artworks_per_student_in_two_years = num_artworks_per_student_per_year * num_years

    # Calculate the total number of artworks for the art club in two years
    total_artworks = num_students * num_artworks_per_student_in_two_years
    result = total_artworks
    return result

print(solution())