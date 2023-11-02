def solution():
    """Bret takes a 9 hour train ride to go to Boston.   He spends 2 hours reading a book, 1 hour to eat his dinner, and 3 hours watching movies on his computer.  How many hours does he have left to take a nap?"""
    # Define the total hours of the train ride
    total_hours = 9

    # Define the hours spent on activities
    reading_hours = 2
    dinner_hours = 1
    movie_hours = 3

    # Calculate the remaining hours for a nap
    remaining_hours = total_hours - (reading_hours + dinner_hours + movie_hours)

    # Display the remaining hours for a nap
    result = remaining_hours
    return result

print(solution())