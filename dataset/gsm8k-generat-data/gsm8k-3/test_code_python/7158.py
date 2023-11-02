def solution():
    """There are 15 students in the art club. By the end of each quarter, each student makes two artworks. If there are four quarters in a school year, how many artworks can the art club collect in two school years?"""
    # Define the number of students and number of quarters per year
    STUDENTS = 15
    QUARTERS_PER_YEAR = 4
    YEARS = 2

    # Calculate the total number of artworks made by each student in a year
    artworks_per_year = 2 * QUARTERS_PER_YEAR

    # Calculate the total number of artworks made by the art club in a year
    total_artworks_per_year = STUDENTS * artworks_per_year

    # Calculate the total number of artworks made by the art club in two school years
    total_artworks = total_artworks_per_year * YEARS

    # Display the total number of artworks
    result = total_artworks
    return result

print(solution())