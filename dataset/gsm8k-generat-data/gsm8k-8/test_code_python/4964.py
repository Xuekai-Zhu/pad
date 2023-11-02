def solution():
    # Define the variables
    members_before_removal = 150
    members_after_removal = members_before_removal - 20
    messages_per_day = 50
    days_in_week = 7

    # Calculate the total number of messages sent per day by the remaining members
    total_messages_per_day = members_after_removal * messages_per_day

    # Calculate the total number of messages sent in a week
    total_messages_per_week = total_messages_per_day * days_in_week
    result = total_messages_per_week
    return result

print(solution())