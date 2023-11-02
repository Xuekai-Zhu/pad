def solution():
    """The teacher assigned a minimum of 25 pages of reading for homework. Harrison read 10 more pages than assigned. Pam read 15 more pages than Harrison and Sam read twice the amount of Pam. How many pages did Sam read?"""
    # Define the minimum number of pages assigned
    min_pages = 25

    # Calculate the number of pages Harrison read
    harrison_pages = min_pages + 10

    # Calculate the number of pages Pam read
    pam_pages = harrison_pages + 15

    # Calculate the number of pages Sam read
    sam_pages = pam_pages * 2

    result = sam_pages
    return result

print(solution())