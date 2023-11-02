def solution():
    """Trevor is a comic book illustrator. In the past three months, he has drawn 220 pages of the comic. The comic he illustrates releases a new issue once a month. The first and second months’ issues were the same number of pages, but the third month’s issue was four pages longer than either of the others. How many pages was the first issue of the comic?"""
    # Define the total number of pages drawn in three months
    total_pages = 220

    # Define the number of pages in the third month's issue
    third_month_pages = 0

    # Calculate the number of pages in each of the first two issues
    first_two_issues_pages = (total_pages - third_month_pages) / 2

    # Calculate the number of pages in the first issue
    first_issue_pages = first_two_issues_pages - 2

    # Display the number of pages in the first issue
    result = first_issue_pages
    return result

print(solution())