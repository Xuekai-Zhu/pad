def solution():
    
    total_guests = 60
    women = total_guests / 2
    men = 15
    children = total_guests - women - men
    men_left = men / 3
    children_left = 5
    guests_left = men_left + children_left
    guests_stayed = total_guests - guests_left
    result = guests_stayed
    return result

print(solution())