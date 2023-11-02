def solution():
    """Meso can type 15 pages in 5 minutes. Tyler can type the same 15 pages in 3 minutes. How many minutes would it take Meso and Tyler to type 40 pages working together?"""
    meso_pages_per_min = 15/5  # Meso types 3 pages per minute
    tyler_pages_per_min = 15/3  # Tyler types 5 pages per minute
    combined_pages_per_min = meso_pages_per_min + tyler_pages_per_min
    total_time = 40 / combined_pages_per_min
    result = total_time
    return result

print(solution())