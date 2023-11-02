def solution():
    """Nico borrows 3 books from the library on Monday. On Monday, he reads the first book with a total of 20 pages. On Tuesday, he reads the second book with a total of 12 pages. On Wednesday, he reads the third book. If he has read a total of 51 pages from Monday to Wednesday, how many pages did he read on Wednesday?"""
    monday_reading = 20
    tuesday_reading = 12
    total_reading = 51
    wednesday_reading = total_reading - monday_reading - tuesday_reading
    result = wednesday_reading
    return result

print(solution())