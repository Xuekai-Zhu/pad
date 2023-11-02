def solution():
    matrix_sequels = 2
    harry_potter_sequels = 7
    harry_potter_box_office_gross = 1342932398
    # Calculate the total box office gross for the Matrix sequels
    matrix_box_office_gross = matrix_sequels * (463517383 + 742128461)
    # Check if Harry Potter is a better investment than the Matrix
    if harry_potter_box_office_gross > matrix_box_office_gross:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())