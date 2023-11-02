def solution():
    """Beth is looking at her book collection and is wondering how many comic books she owns. She has 120 books and 65% are novels. 18 are graphic novels. The rest are comic books. What percentage of comic books does she own?"""
    total_books = 120
    percent_novels = 65
    graphic_novels = 18
    novels = total_books * (percent_novels / 100)
    comic_books = total_books - novels - graphic_novels
    percent_comic_books = (comic_books / total_books) * 100
    result = percent_comic_books
    return result

print(solution())