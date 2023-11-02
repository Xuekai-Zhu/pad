def solution():
    # Calculate the number of pages Jo reads per hour
    pages_per_hour = 30  # Jo reads 30 pages per hour (90 - 60)

    # Calculate the number of hours it will take for Jo to finish the book
    pages_left = 210 - 90  # Jo has 120 pages left to read (210 - 90)
    hours_to_finish = pages_left / pages_per_hour

    result = hours_to_finish
    return result

print(solution())