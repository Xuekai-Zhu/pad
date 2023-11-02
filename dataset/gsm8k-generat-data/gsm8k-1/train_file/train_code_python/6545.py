def solution():
    """John has a party and invites 30 people. Of the people he invited 20% didn't show up. 75% of the people who show up get steak and the rest get chicken. How many people ordered chicken?"""
    total_people = 30
    no_show = total_people * 0.2
    actual_guests = total_people - no_show
    steak_order = actual_guests * 0.75
    chicken_order = actual_guests - steak_order
    result = chicken_order
    return result

print(solution())