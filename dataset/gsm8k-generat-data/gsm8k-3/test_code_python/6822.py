def solution():
    """Meso can type 15 pages in 5 minutes. Tyler can type the same 15 pages in 3 minutes.  How many minutes would it take Meso and Tyler to type 40 pages working together?"""
    # Define Meso's and Tyler's typing speeds in pages per minute
    MESO_SPEED = 3  # 15 pages in 5 minutes
    TYLER_SPEED = 5  # 15 pages in 3 minutes

    # Define the number of pages to be typed
    PAGES = 40

    # Calculate the total time for Meso and Tyler to type 40 pages working together
    total_speed = MESO_SPEED + TYLER_SPEED
    total_time = PAGES / total_speed

    # Display the total time
    result = total_time
    return result

print(solution())