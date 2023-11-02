def solution():
    """Trevor is a comic book illustrator. In the past three months, he has drawn 220 pages of the comic. The comic he illustrates releases a new issue once a month. The first and second months’ issues were the same number of pages, but the third month’s issue was four pages longer than either of the others. How many pages was the first issue of the comic?"""
    # Calculate the total number of pages for the three months
    total_pages = 220

    # Assume the first and second month's issue were the same length, and call that length x
    first_month_pages = x
    second_month_pages = x
    
    # The third month's issue was 4 pages longer than the first two, so its length was x + 4
    third_month_pages = x + 4
    
    # The total number of pages for the three months was 220, so we can set up an equation
    # x + x + (x + 4) = 220
    # which simplifies to
    # 3x + 4 = 220
    # Solving for x gives x = 72
    
    # Therefore, the first issue of the comic was 72 pages
    result = 72
    return result

print(solution())