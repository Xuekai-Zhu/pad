def solution():
    """Elmer has a pond that initially contained 2400 pollywogs, but these pollywogs matured into toads and left the pond at a constant rate of 50 pollywogs per day. In addition, Elmer has a son named Melvin, who loves to catch pollywogs, remove them from the pond, and release them into a nearby stream. For the first 20 days, Melvin caught 10 pollywogs per day and released them into the stream. How many days did it take for all of the pollywogs to disappear from the pond?"""
    # Define the initial number of pollywogs and the rate at which they leave the pond
    initial_pollywogs = 2400
    leaving_rate = 50

    # Define the number of days Melvin catches pollywogs for
    catching_days = 20

    # Define the number of pollywogs Melvin catches each day
    catch_rate = 10

    # Calculate the number of pollywogs that leave the pond during the catching period
    leaving_during_catching = catch_rate * catching_days

    # Calculate the number of pollywogs that are left after the initial ones leave and Melvin catches some
    remaining_pollywogs = initial_pollywogs - leaving_during_catching

    # Calculate the number of days it will take for the remaining pollywogs to leave the pond
    days_to_empty = remaining_pollywogs / leaving_rate

    # Add the number of days it took Melvin to catch pollywogs
    total_days = catching_days + days_to_empty

    # return the result
    result = total_days
    return result

print(solution())