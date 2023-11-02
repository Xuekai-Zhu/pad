def solution():
    
    remaining_members = 150 - 20
    messages_per_day = 50
    total_messages_in_week = remaining_members * messages_per_day * 7
    result = total_messages_in_week
    return result

print(solution())