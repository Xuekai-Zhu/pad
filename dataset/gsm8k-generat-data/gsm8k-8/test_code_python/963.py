def solution():
    # Calculate the number of women at the event
    men = 40
    women = men / 2

    # Calculate the number of children at the event
    total_guests = 80
    children = total_guests - men - women

    # Add 10 children to the guest list
    children += 10
    
    result = children
    return result

print(solution())