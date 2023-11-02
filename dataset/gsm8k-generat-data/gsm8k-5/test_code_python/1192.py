def solution():
    total_attendees = 120

    # Calculate the number of men
    men = total_attendees * (1/3)

    # Calculate the number of women
    women = total_attendees * (1/2)

    # Calculate the number of children
    children = total_attendees - men - women
    result = children
    return result

print(solution())