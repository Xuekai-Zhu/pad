def solution():
    """Wickham is throwing a huge Christmas party. He invites 30 people. Everyone attends the party, and half of the guests bring a plus one (one other person). He plans to serve a 3-course meal for the guests. If he uses a new plate for every course, how many plates does he need in total for his guests?"""
    total_guests = 30
    plus_ones = total_guests / 2
    total_meals_served = 3 * (total_guests + plus_ones)
    plates_needed = total_meals_served
    result = plates_needed
    return result

print(solution())