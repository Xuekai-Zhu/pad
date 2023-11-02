def solution():
    """Jim reads at a rate of 40 pages an hour. He reads a total of 600 pages per week. He increases his reading speed to 150% of its former speed but reads 4 hours less per week. How many pages does he read a week now?"""
    # Define Jim's initial reading speed and total weekly pages read
    initial_speed = 40
    initial_hours = 600 / initial_speed

    # Define Jim's new reading speed and total weekly hours read
    new_speed = initial_speed * 1.5
    new_hours = initial_hours - 4

    # Calculate the new total weekly pages read
    new_pages = new_speed * new_hours

    # return the result
    result = new_pages
    return result

print(solution())