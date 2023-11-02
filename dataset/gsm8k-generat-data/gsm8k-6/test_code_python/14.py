def solution():
    # Calculate the number of minutes Joy will need to read 120 pages
    minutes_needed = (120 / 8) * 20

    # Convert minutes to hours
    hours_needed = minutes_needed / 60

    result = hours_needed
    return result

print(solution())