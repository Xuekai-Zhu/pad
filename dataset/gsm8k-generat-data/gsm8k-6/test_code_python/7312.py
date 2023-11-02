def solution():
    # Calculate the total number of pages in the first two issues
    first_two_issues = 220 - 4  # the third month's issue was four pages longer than either of the others
    first_two_issues = first_two_issues // 2  # the first and second months’ issues were the same number of pages

    # Calculate the number of pages in the first issue
    first_issue = first_two_issues // 2

    result = first_issue
    return result

print(solution())