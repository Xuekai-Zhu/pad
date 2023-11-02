def solution():
    """John has a party and invites 30 people. Of the people he invited 20% didn't show up. 75% of the people who show up get steak and the rest get chicken. How many people ordered chicken?"""
    total_invited = 30
    no_show = 0.2 * total_invited
    total_showed = total_invited - no_show
    steak_order = 0.75 * total_showed
    chicken_order = total_showed - steak_order
    result = chicken_order
    return result

print(solution())