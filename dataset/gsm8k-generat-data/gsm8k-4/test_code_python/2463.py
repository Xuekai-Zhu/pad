def solution():
    """A group of 300 athletes spent Saturday night at Ultimate Fitness Camp. The next morning, for 4 hours straight, they left the camp at a rate of 28 athletes per hour. Over the next 7 hours, a new group of athletes trickled into the camp at a rate of 15 athletes per hour. Immediately thereafter, the camp gate was shut and everyone went to bed. What is the difference in the total number of athletes in the camp over the two nights?"""
    
    # Define the initial number of athletes
    initial_athletes = 300

    # Calculate the number of athletes who left on the second day
    athletes_left = 4 * 28

    # Calculate the number of athletes who arrived on the second day
    athletes_arrived = 7 * 15

    # Calculate the total number of athletes at the end of the second day
    total_athletes = initial_athletes - athletes_left + athletes_arrived

    # Calculate the difference in the total number of athletes over the two nights
    difference = total_athletes - initial_athletes

    # return the result
    result = difference
    return result

print(solution())