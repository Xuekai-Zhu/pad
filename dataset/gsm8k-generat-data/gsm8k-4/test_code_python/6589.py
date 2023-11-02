def solution():
    """Billy has 8 hours of free time on each day of the weekend. He wants to spend 75% of his time playing video games and the rest of his time reading. He can read 60 pages an hour and his books all contain 80 pages. How many books does he read?"""
    # Define the total number of free hours
    total_hours = 8 * 2

    # Calculate the number of hours spent playing video games
    game_hours = total_hours * 0.75

    # Calculate the number of hours spent reading
    reading_hours = total_hours - game_hours

    # Calculate the total number of pages read
    total_pages = reading_hours * 60 * 2

    # Calculate the number of books read
    books = total_pages / 80

    # Return the result
    result = round(books)
    return result

print(solution())