def solution():
    """Brian likes to read books. He read one book that had 20 chapters, 
    two books that had 15 chapters each, and one book that had half the chapters 
    of the three previous books put together. How many chapters of books did Brian read?"""
    
    # Define the number of chapters in the first book
    book1_chapters = 20
    
    # Define the number of chapters in each of the second and third books
    book2_chapters = 15
    book3_chapters = 15
    
    # Calculate the total number of chapters in the second and third books
    book2_and_3_chapters = book2_chapters + book3_chapters
    
    # Calculate the total number of chapters in the first three books combined
    first_three_books = book1_chapters + book2_and_3_chapters
    
    # Calculate the number of chapters in the fourth book
    book4_chapters = first_three_books / 2
    
    # Calculate the total number of chapters Brian read
    total_chapters = book1_chapters + book2_chapters + book3_chapters + book4_chapters
    
    # return the result
    result = total_chapters
    return result

print(solution())