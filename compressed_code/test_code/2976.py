def solution():
    
    total_guests = 50
    women = total_guests // 2
    men = 15
    children = total_guests - women - men
    men_left = men // 5
    children_left = 4
    total_left = men_left + children_left
    stayed = total_guests - total_left
    result = stayed
    return result

print(solution())