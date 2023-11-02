def solution():
    """Oleg is an event organizer. He is organizing an event with 80 guests where 40 of them are men, half the number of men are women, and the rest are children. If he added 10 children to the guest list, how many children will there be at the event?"""
    total_guests = 80
    men = 40
    women = men / 2
    children = total_guests - men - women
    new_children = children + 10
    result = new_children
    return result

print(solution())