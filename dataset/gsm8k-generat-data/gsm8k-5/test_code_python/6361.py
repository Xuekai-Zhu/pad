def solution():
    assigned_reading = 25  # The assigned reading is 25 pages
    harrison_reading = assigned_reading + 10  # Harrison read 10 more pages than assigned
    pam_reading = harrison_reading + 15  # Pam read 15 more pages than Harrison
    sam_reading = 2 * pam_reading  # Sam read twice the amount of Pam

    result = sam_reading
    return result

print(solution())