def solution():
    total_guests = 60
    men = 15
    women = total_guests / 2
    children = total_guests - men - women
    men_leaving = men / 3
    children_leaving = 5
    guests_remaining = total_guests - (men_leaving + children_leaving)
    result = guests_remaining
    return result

print(solution())