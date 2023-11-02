def solution():
    # Calculate the total number of artworks made by one student in a year
    art_per_student_per_year = 2 * 4

    # Calculate the total number of artworks made by all students in a year
    total_art_per_year = art_per_student_per_year * 15

    # Calculate the total number of artworks made by all students in two years
    total_art_per_two_years = total_art_per_year * 2

    result = total_art_per_two_years
    return result

print(solution())