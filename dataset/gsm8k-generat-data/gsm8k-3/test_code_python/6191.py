def solution():
    """The stadium seats 60,000 fans, but only 75% of the seats were sold for the music show. Because of the threat of rain, 5,000 fans stayed home. How many attended the show?"""
    # Define the number of seats and the percentage sold
    TOTAL_SEATS = 60000
    PERCENT_SOLD = 0.75

    # Calculate the number of seats sold
    seats_sold = int(TOTAL_SEATS * PERCENT_SOLD)

    # Calculate the number of fans who attended the show
    fans_attended = seats_sold - 5000

    # Display the number of fans who attended the show
    result = fans_attended
    return result

print(solution())