def solution():
    """The stadium seats 60,000 fans, but only 75% of the seats were sold for the music show. Because of the threat of rain, 5,000 fans stayed home. How many attended the show?"""
    # Define the total number of seats in the stadium
    total_seats = 60000

    # Calculate the number of seats sold for the music show
    seats_sold = total_seats * 0.75

    # Calculate the actual attendance
    actual_attendance = seats_sold - 5000

    # return the result
    result = actual_attendance
    return result

print(solution())