def solution():
    """Xander read 20% of his 500-page book in one hour. The next night he read another 20% of the book. On the third night, he read 30% of his book. How many pages does he have left to read?"""
    # Define the total number of pages and the percentage read on each night
    total_pages = 500
    first_night_percentage = 0.2
    second_night_percentage = 0.2
    third_night_percentage = 0.3

    # Calculate the number of pages read on each night
    first_night_pages = total_pages * first_night_percentage
    second_night_pages = total_pages * second_night_percentage
    third_night_pages = total_pages * third_night_percentage

    # Calculate the total number of pages read
    total_read = first_night_pages + second_night_pages + third_night_pages

    # Calculate the number of pages left to read
    pages_left = total_pages - total_read

    # return the result
    result = pages_left
    return result

print(solution())