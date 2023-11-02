def solution():
    """A simple folding newspaper or tabloid can be made by folding a piece of paper vertically and unfolding. Then, say, page 1 is printed on the left back, page 2 is printed on the left front, and then, perhaps page 32 is printed on the right back, and page 31 is printed on the right front. How many pieces of paper would be used in a 32-page tabloid?"""
    pages_per_paper = 4
    total_pages = 32
    papers_needed = total_pages / pages_per_paper
    result = papers_needed
    return result

print(solution())