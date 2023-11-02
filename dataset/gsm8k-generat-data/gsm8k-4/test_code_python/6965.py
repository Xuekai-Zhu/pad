def solution():
    """Julie runs the school newspaper. In preparation for printing the next issue of The School News, she bought two boxes of standard paper, each containing 5 packages, with 250 sheets of paper per package. If this issue of The School News uses 25 sheets of paper to print one newspaper, how many newspapers can Julie print with the paper that she purchased?"""
    # Define the number of sheets of paper Julie purchase
    sheets_of_paper = 2*5*250

    # Define the number of newspapers that can be printed
    newspapers = sheets_of_paper // 25

    result = newspapers
    return result

print(solution())