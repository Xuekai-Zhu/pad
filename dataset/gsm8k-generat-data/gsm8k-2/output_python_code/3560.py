def solution():
    """The novel that everyone is reading for English class has half as many pages as their history book. Their science book has 4 times the amount of pages as their novel. If the history book has 300 pages, how many pages does their science book have?"""
    history_pages = 300
    novel_pages = history_pages / 2
    science_pages = novel_pages * 4
    result = science_pages
    return result

print(solution())