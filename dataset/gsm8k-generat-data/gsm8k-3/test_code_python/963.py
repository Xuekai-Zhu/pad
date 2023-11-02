def solution():
    """Oleg is organizing an event with 80 guests where 40 of them are men, half the number of men are women, and the rest are children. If he added 10 children to the guest list, how many children will there be at the event?"""
    # Determine the number of men and women
    num_men = 40
    num_women = num_men / 2

    # Determine the number of children before adding 10
    num_children = 80 - num_men - num_women

    # Add 10 children to the guest list
    num_children += 10

    # Display the number of children at the event
    result = num_children
    return result

print(solution())