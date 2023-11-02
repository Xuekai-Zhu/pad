def solution():
    
    total_guests = 50
    women = total_guests // 2
    men = 15
    children = total_guests - women - men
    men_left = men // 5
    children_left = 4
    remaining_guests = total_guests - men_left - children_left
    result = remaining_guests
    return result

print(solution())