def solution():
    """Wickham is throwing a huge Christmas party. He invites 30 people. Everyone attends the party, and half of the guests bring a plus one (one other person). He plans to serve a 3-course meal for the guests. If he uses a new plate for every course, how many plates does he need in total for his guests?"""
    num_guests = 30
    num_plus_ones = num_guests // 2
    total_guests = num_guests + num_plus_ones
    num_courses = 3
    plates_per_guest = num_courses
    total_plates = total_guests * plates_per_guest
    result = total_plates
    return result

print(solution())