def solution():
    """Beth is looking at her book collection and is wondering how many comic books she owns. She has 120 books and 65% are novels. 18 are graphic novels. The rest are comic books. What percentage of comic books does she own?"""
    total_books = 120
    novels = int(total_books * 0.65)
    graphic_novels = 18
    comic_books = total_books - novels - graphic_novels
    comic_percentage = (comic_books / total_books) * 100
    result = comic_percentage
    return result

print(solution())