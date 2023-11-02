def solution():
    pages_per_hour = 12
    hours = 2
    speed_increase_factor = 3

    # Calculate the new pages per hour reading speed
    new_speed = pages_per_hour * speed_increase_factor

    # Calculate the total number of pages Tom can read in 2 hours at the new speed
    total_pages = new_speed * hours
    result = total_pages
    return result

print(solution())