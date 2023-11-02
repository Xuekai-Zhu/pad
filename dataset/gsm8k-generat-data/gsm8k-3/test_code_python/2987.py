def solution():
    """Beth is looking at her book collection and is wondering how many comic books she owns. She has 120 books and 65% are novels. 18 are graphic novels. The rest are comic books. What percentage of comic books does she own?"""
    # Calculate the number of novels
    novels = 120 * 0.65

    # Calculate the number of comic books
    comic_books = 120 - novels - 18

    # Calculate the percentage of comic books
    percentage_comic_books = (comic_books / 120) * 100

    # Display the percentage of comic books
    result = percentage_comic_books
    return result

print(solution())