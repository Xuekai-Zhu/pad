def solution():
    """Nico borrows 3 books from the library on Monday. On Monday, he reads the first book with a total of 20 pages. On Tuesday, he reads the second book with a total of 12 pages. On Wednesday, he reads the third book. If he has read a total of 51 pages from Monday to Wednesday, how many pages did he read on Wednesday?"""
    monday_pages = 20
    tuesday_pages = 12
    total_pages = 51
    wednesday_pages = total_pages - monday_pages - tuesday_pages
    result = wednesday_pages
    return result

print(solution())