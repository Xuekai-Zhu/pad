def solution():
    """Trevor is a comic book illustrator. In the past three months, he has drawn 220 pages of the comic. The comic he illustrates releases a new issue once a month.
    The first and second months’ issues were the same number of pages, but the third month’s issue was four pages longer than either of the others. How many pages was the first issue of the comic?"""
    total_pages = 220
    third_month_pages = (total_pages / 3) + 2
    first_two_months_pages = (total_pages - third_month_pages) / 2
    first_issue_pages = first_two_months_pages - 2
    result = first_issue_pages
    return result

print(solution())