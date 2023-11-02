def solution():
    """Jim reads at a rate of 40 pages an hour.  He reads a total of 600 pages per week.  He increases his reading speed to 150% of its former speed but reads 4 hours less per week.  How many pages does he read a week now?"""
    # Define Jim's initial reading rate and the total pages he reads per week
    initial_rate = 40
    total_pages = 600

    # Calculate Jim's initial reading time and the number of pages he reads per hour at his initial rate
    initial_time = total_pages / initial_rate
    initial_pages_per_hour = total_pages / initial_time / 7

    # Calculate Jim's new reading rate and time, accounting for the decrease in hours
    new_rate = initial_rate * 1.5
    new_time = initial_time - 4 / 7

    # Calculate the number of pages Jim reads per hour at his new rate
    new_pages_per_hour = (total_pages / new_time) / 7

    # Calculate the total number of pages Jim reads per week at his new rate
    new_total_pages = new_pages_per_hour * 7

    # Display the total number of pages Jim reads per week at his new rate
    result = new_total_pages
    return result

print(solution())