def solution():
    attendees = 100
    women = attendees * 0.5
    men = attendees * 0.35
    children = attendees - women - men
    result = children
    return result

print(solution())