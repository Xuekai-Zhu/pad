def solution():
    """Meso can type 15 pages in 5 minutes. Tyler can type the same 15 pages in 3 minutes. How many minutes would it take Meso and Tyler to type 40 pages working together?"""
    meso_speed = 15/5 # pages per minute
    tyler_speed = 15/3 # pages per minute
    combined_speed = meso_speed + tyler_speed # pages per minute
    total_pages = 40
    time_taken = total_pages / combined_speed # minutes
    result = time_taken
    return result

print(solution())