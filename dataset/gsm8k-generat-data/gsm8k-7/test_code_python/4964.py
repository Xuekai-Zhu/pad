def solution():
    num_members = 150
    num_removed = 20
    num_remaining = num_members - num_removed
    num_messages_per_day = 50
    num_days = 7

    # Calculate the total number of messages the remaining members would send in a day
    total_messages_per_day = num_remaining * num_messages_per_day

    # Calculate the total number of messages the remaining members would send in a week
    total_messages_per_week = total_messages_per_day * num_days
    result = total_messages_per_week
    return result

print(solution())