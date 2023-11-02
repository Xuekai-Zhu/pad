def solution():
    """Grace can read a 200-page book in 20 hours. How long would it take her to finish reading a 250-page book at this constant rate?"""
    # Define the number of pages and time it takes Grace to read a 200-page book
    num_pages1 = 200
    time1 = 20

    # Calculate the rate at which Grace reads
    rate = num_pages1 / time1

    # Define the number of pages in the second book
    num_pages2 = 250

    # Calculate the time it takes Grace to read the second book
    time2 = num_pages2 / rate

    # Display the time it takes Grace to read the second book
    result = time2
    return result

print(solution())