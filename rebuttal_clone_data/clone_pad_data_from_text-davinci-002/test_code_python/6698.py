def solution():
    messages = 98
    messages_read_per_day = 20
    messages_received_per_day = 6
    
    days_to_read = messages / messages_read_per_day
    days_to_receive = messages / messages_received_per_day
    
    total_days = days_to_read + days_to_receive
    result = total_days
    return result

print(solution())