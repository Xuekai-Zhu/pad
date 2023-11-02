def solution():
    total_pages = 220  # Trevor has drawn a total of 220 pages in the past three months
    third_month = 4  # The third month's issue was four pages longer than the first and second months
    total_pages -= third_month  # Deduct the third month's pages from the total
    remaining_pages = total_pages / 2  # Divide the remaining pages equally between the first two months
    first_month = remaining_pages / 2  # The first and second months had the same number of pages

    result = first_month
    return result

print(solution())