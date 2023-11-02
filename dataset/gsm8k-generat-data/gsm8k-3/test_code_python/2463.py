def solution():
    """A group of 300 athletes spent Saturday night at Ultimate Fitness Camp. The next morning, for 4 hours straight, they left the camp at a rate of 28 athletes per hour. Over the next 7 hours, a new group of athletes trickled into the camp at a rate of 15 athletes per hour. Immediately thereafter, the camp gate was shut and everyone went to bed. What is the difference in the total number of athletes in the camp over the two nights?"""
    # Calculate the number of athletes leaving the camp on Sunday morning
    leaving_athletes = 4 * 28

    # Calculate the number of athletes arriving at the camp on Sunday
    arriving_athletes = 7 * 15

    # Calculate the total number of athletes at the camp on Sunday night
    sunday_athletes = 300 - leaving_athletes + arriving_athletes

    # Calculate the difference between the total number of athletes on Saturday and Sunday nights
    difference = sunday_athletes - 300

    # Display the difference in the total number of athletes
    result = difference
    return result

print(solution())