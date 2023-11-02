def solution():
    """Wickham is throwing a huge Christmas party. He invites 30 people. Everyone attends the party, and half of the guests bring a plus one (one other person). He plans to serve a 3-course meal for the guests. If he uses a new plate for every course, how many plates does he need in total for his guests?"""
    # Define the number of guests and plus ones
    guests = 30
    plus_ones = guests * 0.5

    # Calculate the total number of people attending the party
    total_attendees = guests + plus_ones

    # Calculate the total number of plates needed for each course
    plates_per_course = total_attendees * 3

    # Return the total number of plates needed
    result = plates_per_course
    return result

print(solution())