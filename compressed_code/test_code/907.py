def solution():
    
    total_attendees = 120
    men = total_attendees / 3
    women = total_attendees / 2
    children = total_attendees - men - women
    result = children
    return result

print(solution())