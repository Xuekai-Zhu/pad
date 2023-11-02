def solution():
    """The teacher assigned a minimum of 25 pages of reading for homework. Harrison read 10 more pages than assigned. Pam read 15 more pages than Harrison and Sam read twice the amount of Pam. How many pages did Sam read?"""
    assigned_reading = 25
    harrison_reading = assigned_reading + 10
    pam_reading = harrison_reading + 15
    sam_reading = pam_reading * 2
    result = sam_reading
    return result

print(solution())