def solution():
    
    total_visitors = 500
    sick_percentage = 40
    sick_visitors = total_visitors * (sick_percentage / 100)
    healthy_visitors = total_visitors - sick_visitors
    result = healthy_visitors
    return result

print(solution())