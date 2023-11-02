def solution():
    total_guests = 50
    men = 15
    women = total_guests - men
    children = total_guests - (men + women)
    departed_men = men / 5
    departed_children = children / 4
    remained_men = men - departed_men
    remained_children = children - departed_children
    remained_total = total_guests - (departed_men + departed_children)
    result = remained_total
    return result

print(solution())