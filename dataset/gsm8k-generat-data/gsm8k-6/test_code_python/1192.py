def solution():
    total_attendees = 120  # total number of people at the party
    men = (1/3) * total_attendees  # number of men
    women = 0.5 * total_attendees  # number of women
    children = total_attendees - men - women  # number of children
    result = children
    return result

print(solution())