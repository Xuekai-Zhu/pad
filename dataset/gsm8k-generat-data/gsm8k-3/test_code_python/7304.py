def solution():
    """Elmer has a pond that initially contained 2400 pollywogs, but these pollywogs matured into toads and left the pond at a constant rate of 50 pollywogs per day.  In addition, Elmer has a son named Melvin, who loves to catch pollywogs, remove them from the pond, and release them into a nearby stream.  For the first 20 days, Melvin caught 10 pollywogs per day and released them into the stream.  How many days did it take for all of the pollywogs to disappear from the pond?"""
    # Define the initial number of pollywogs and the rate at which they leave the pond
    initial_pollywogs = 2400
    leaving_rate = 50

    # Calculate the number of days it takes for all the pollywogs to leave the pond on their own
    leaving_days = initial_pollywogs // leaving_rate

    # Define the number of pollywogs caught and released per day by Melvin
    caught_rate = 10

    # Calculate the number of pollywogs caught and released by Melvin during the leaving period
    melvin_pollywogs = caught_rate * 20

    # Calculate the remaining number of pollywogs after Melvin catches and releases some
    remaining_pollywogs = initial_pollywogs - melvin_pollywogs

    # Calculate the number of days it takes for the remaining pollywogs to leave the pond
    remaining_days = remaining_pollywogs // leaving_rate

    # Calculate the total number of days it takes for all the pollywogs to disappear from the pond
    total_days = 20 + leaving_days + remaining_days

    # Display the total number of days
    result = total_days
    return result

print(solution())