def solution():
    
    members_before_removal = 150
    members_removed = 20
    members_remaining = members_before_removal - members_removed
    messages_per_day_per_member = 50
    days_in_a_week = 7
    total_messages = members_remaining * messages_per_day_per_member * days_in_a_week
    result = total_messages
    return result

print(solution())