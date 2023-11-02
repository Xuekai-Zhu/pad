def solution():
    
    total_guests = 80
    men = 40
    women = men / 2
    children = total_guests - men - women
    children += 10
    result = children
    return result

print(solution())