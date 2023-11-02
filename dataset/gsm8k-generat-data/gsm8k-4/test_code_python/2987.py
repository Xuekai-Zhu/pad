def solution():
    """Beth is looking at her book collection and is wondering how many comic books she owns. She has 120 books and 65% are novels. 18 are graphic novels. The rest are comic books. What percentage of comic books does she own?"""
    # Define the total number of books and the number of novels
    total_books = 120
    novel_books = total_books * 0.65

    # Calculate the number of comic books
    comic_books = total_books - novel_books - 18

    # Calculate the percentage of comic books
    comic_percentage = (comic_books / total_books) * 100

    # Return the result
    result = comic_percentage
    return result

print(solution())