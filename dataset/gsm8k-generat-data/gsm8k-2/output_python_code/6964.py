def solution():
    """Julie runs the school newspaper. In preparation for printing the next issue of The School News, she bought two boxes of standard paper, each containing 5 packages, with 250 sheets of paper per package. If this issue of The School News uses 25 sheets of paper to print one newspaper, how many newspapers can Julie print with the paper that she purchased?"""
    sheets_per_package = 250
    packages_per_box = 5
    boxes = 2
    total_sheets = sheets_per_package * packages_per_box * boxes
    sheets_per_newspaper = 25
    newspapers_that_can_be_printed = total_sheets // sheets_per_newspaper
    result = newspapers_that_can_be_printed
    return result

print(solution())