def solution():
    """Liza reads 20 pages in an hour, and Suzie reads 15 pages in an hour. How many more pages does Liza read than Suzie in 3 hours?"""
    # Define the number of pages read per hour by Liza and Suzie
    liza_rate = 20
    suzie_rate = 15

    # Calculate the number of pages read by Liza and Suzie in 3 hours
    liza_total = liza_rate * 3
    suzie_total = suzie_rate * 3

    # Calculate the difference in the number of pages read by Liza and Suzie
    difference = liza_total - suzie_total

    # Display the difference in the number of pages read
    result = difference
    return result

print(solution())