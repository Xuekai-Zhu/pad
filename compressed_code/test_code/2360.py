def solution():
    
    total_visitors = 500
    ill_percentage = 0.4
    ill_visitors = total_visitors * ill_percentage
    healthy_visitors = total_visitors - ill_visitors
    result = healthy_visitors
    return result

print(solution())