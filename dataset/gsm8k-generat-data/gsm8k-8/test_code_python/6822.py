def solution():
    # Calculate the combined typing speed
    combined_speed = 15/5 + 15/3

    # Calculate the time it would take to type 1 page with the combined speed
    time_per_page = 1/combined_speed

    # Calculate the total time it would take to type 40 pages
    total_time = 40 * time_per_page
    result = total_time
    return result

print(solution())