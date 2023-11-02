def solution():
    """There are 15 students in the art club. By the end of each quarter, each student makes two artworks. If there are four quarters in a school year, how many artworks can the art club collect in two school years?"""
    # Define the number of students in the art club
    num_students = 15

    # Define the number of quarters
    num_quarters = 4

    # Define the number of artworks per student per quarter
    num_artworks_per_student_per_quarter = 2

    # Calculate the total number of artworks in one school year
    num_artworks_per_year = num_students * num_artworks_per_student_per_quarter * num_quarters

    # Calculate the total number of artworks in two school years
    num_artworks_two_years = num_artworks_per_year * 2

    result = num_artworks_two_years
    return result

print(solution())