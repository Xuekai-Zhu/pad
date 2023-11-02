def solution():
    """Grace can read a 200-page book in 20 hours. How long would it take her to finish reading a 250-page book at this constant rate?"""
    # Define the number of pages and hours it takes Grace to read a book
    pages = 200
    hours = 20

    # Calculate the rate at which Grace reads
    rate = pages / hours

    # Use the rate to calculate how long it would take Grace to read a 250-page book
    time = 250 / rate

    # Round the result to 2 decimal places
    result = round(time, 2)
    return result

print(solution())