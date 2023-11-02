def solution():
    time_reading = 1/6 # Miles is going to spend 1/6 of a day reading
    time_per_book = time_reading / 3 # Miles will spend 1/3 of his time reading each book type
    pages_per_hour_novel = 21 # Miles reads 21 pages an hour when he reads a novel
    pages_per_hour_graphic_novel = 30 # Miles reads 30 pages an hour when he reads a graphic novel
    pages_per_hour_comic_book = 45 # Miles reads 45 pages an hour when he reads a comic book

    # Calculate the total number of pages Miles will read of each book type
    pages_novel = pages_per_hour_novel * time_per_book
    pages_graphic_novel = pages_per_hour_graphic_novel * time_per_book
    pages_comic_book = pages_per_hour_comic_book * time_per_book

    # Calculate the total number of pages Miles will read
    total_pages = pages_novel + pages_graphic_novel + pages_comic_book
    result = total_pages
    return result

print(solution())