def solution():
    """The teacher assigned a minimum of 25 pages of reading for homework.  Harrison read 10 more pages than assigned.  Pam read 15 more pages than Harrison and Sam read twice the amount of Pam.  How many pages did Sam read?"""
    # Define the minimum number of pages assigned
    MIN_PAGES = 25

    # Calculate Harrison's number of pages read
    harrison_pages = MIN_PAGES + 10

    # Calculate Pam's number of pages read
    pam_pages = harrison_pages + 15

    # Calculate Sam's number of pages read
    sam_pages = pam_pages * 2

    # Display Sam's number of pages read
    result = sam_pages
    return result

print(solution())