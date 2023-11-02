def solution():
    members_before_removal = 150  # Number of members in the group before removal
    members_after_removal = members_before_removal - 20  # Number of members remaining after removal
    messages_per_member_per_day = 50  # Number of messages each member posts per day
    days_per_week = 7  # Number of days in a week

    # Calculate the total number of messages the remaining members would send per day
    total_messages_per_day = members_after_removal * messages_per_member_per_day

    # Calculate the total number of messages the remaining members would send in a week
    total_messages_per_week = total_messages_per_day * days_per_week
    result = total_messages_per_week
    return result

print(solution())