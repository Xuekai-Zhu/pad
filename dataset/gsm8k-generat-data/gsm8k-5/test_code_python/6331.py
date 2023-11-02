def solution():
    anna_speed = 1  # Anna can read 1 page in 1 minute
    carole_speed = anna_speed / 2  # Carole can read at half Brianna's speed

    brianna_pages_per_minute = anna_speed + carole_speed
    # Brianna can read at the combined speed of Anna and Carole

    pages_in_book = 100  # The book has 100 pages

    # Calculate how long Brianna takes to read the 100-page book
    time_taken = pages_in_book / brianna_pages_per_minute
    result = time_taken
    return result

print(solution())