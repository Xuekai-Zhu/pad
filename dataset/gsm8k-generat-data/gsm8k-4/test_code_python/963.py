def solution():
    """Oleg is an event organizer. He is organizing an event with 80 guests where 40 of them are men, half the number of men are women, and the rest are children. If he added 10 children to the guest list, how many children will there be at the event?"""
    # Define the number of men and women
    men = 40
    women = men * 0.5

    # Calculate the number of children
    children = 80 - men - women

    # Add 10 children to the guest list
    children += 10

    # Return the number of children at the event
    result = children
    return result

print(solution())