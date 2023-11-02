def solution():
    
    total_guests = 80
    men = 40
    women = men / 2
    children = total_guests - men - women
    new_children = children + 10
    result = new_children
    return result

print(solution())