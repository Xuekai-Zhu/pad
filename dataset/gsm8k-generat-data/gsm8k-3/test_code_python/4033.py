def solution():
    """Tom decided to send his wife 2 dozen roses every day for the week.  How many total roses did he send?"""
    # Define the number of dozens of roses Tom sends each day
    ROSES_PER_DAY = 2 * 12

    # Calculate the total number of roses Tom sends over the week
    total_roses = ROSES_PER_DAY * 7

    # Display the total number of roses
    result = total_roses
    return result

print(solution())