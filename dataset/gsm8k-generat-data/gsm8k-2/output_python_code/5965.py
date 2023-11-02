def solution():
    """Xander read 20% of his 500-page book in one hour. The next night he read another 20% of the book. On the third night, he read 30% of his book. How many pages does he have left to read?"""
    total_pages = 500
    first_night_pages = total_pages * 0.2
    second_night_pages = total_pages * 0.2
    third_night_pages = total_pages * 0.3
    total_read = first_night_pages + second_night_pages + third_night_pages
    pages_left = total_pages - total_read
    result = pages_left
    return result

print(solution())