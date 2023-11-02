def solution():
    """Wickham is throwing a huge Christmas party. He invites 30 people. Everyone attends the party, and half of the guests bring a plus one (one other person). He plans to serve a 3-course meal for the guests. If he uses a new plate for every course, how many plates does he need in total for his guests?"""
    # Define the number of guests and additional plus ones
    guests = 30
    plus_ones = guests / 2

    # Calculate the total number of people at the party
    total_people = guests + plus_ones

    # Calculate the total number of plates needed
    plates_needed = total_people * 3

    # return the result
    result = plates_needed
    return result

print(solution())