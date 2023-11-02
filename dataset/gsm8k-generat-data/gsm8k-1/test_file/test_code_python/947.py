def solution():
    """The book is printed on paper that, when stacked, is 100 pages to the inch. Each paper is printed on both sides, with one page of the book printed on each side.
     How many pages are in the book, if it is 1.5 inches thick?"""

    pages_per_inch = 100
    thickness_in_inches = 1.5
    pages_per_paper = 2
    total_pages = thickness_in_inches * pages_per_inch * pages_per_paper
    result = total_pages
    return result

print(solution())