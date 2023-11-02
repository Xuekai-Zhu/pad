def solution():
    """Julie runs the school newspaper. In preparation for printing the next issue of The School News, she bought two boxes of standard paper, each containing 5 packages, with 250 sheets of paper per package.  If this issue of The School News uses 25 sheets of paper to print one newspaper, how many newspapers can Julie print with the paper that she purchased?"""
    # Define the number of sheets of paper in each package
    SHEETS_PER_PACKAGE = 250

    # Define the number of packages per box
    PACKAGES_PER_BOX = 5

    # Define the number of boxes purchased
    BOXES_PURCHASED = 2

    # Calculate the total number of sheets of paper purchased
    total_sheets = SHEETS_PER_PACKAGE * PACKAGES_PER_BOX * BOXES_PURCHASED

    # Calculate the number of newspapers that can be printed
    newspapers = total_sheets // 25

    # Display the number of newspapers that can be printed
    result = newspapers
    return result

print(solution())