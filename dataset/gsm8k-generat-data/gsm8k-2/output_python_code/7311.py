def solution():
    """Trevor is a comic book illustrator. In the past three months, he has drawn 220 pages of the comic. The comic he illustrates releases a new issue once a month. The first and second months’ issues were the same number of pages, but the third month’s issue was four pages longer than either of the others. How many pages was the first issue of the comic?"""
    total_pages = 220
    third_month_extra = 4

    # Let first and second month's pages be x
    # Then third month's pages will be x + 4
    # So total pages will be 3x + 4
    # We know that 3x + 4 = 220
    # Solving for x, we get x = (220 - 4) / 3 = 72

    first_month_pages = 72
    result = first_month_pages
    return result

print(solution())