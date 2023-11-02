def solution():
    """Tom, an avid stamp collector, has 3,000 stamps in his collection. He is very sad because he lost his job last Friday. His brother, Mike, and best friend, Harry, try to cheer him up with more stamps. Harry’s gift to Tom is 10 more stamps than twice Mike’s gift. If Mike has given Tom 17 stamps, how many stamps does Tom’s collection now have?"""
    # Define the initial number of stamps
    initial_stamps = 3000

    # Define the number of stamps Mike gave Tom
    mike_gift = 17

    # Calculate the number of stamps Harry gave Tom
    harry_gift = 2 * mike_gift + 10

    # Calculate the total number of stamps Tom has now
    total_stamps = initial_stamps + mike_gift + harry_gift

    # Display the total number of stamps
    result = total_stamps
    return result

print(solution())