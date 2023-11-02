def solution():
    """After violating the group's policies, 20 members of a Facebook group were removed by the group's admin. If each member posted 50 messages per day in the group and the number of members in the group was 150 before the admin removed some, calculate the total number of messages the remaining members would send in a week."""
    # Define the number of members in the group and the number of messages per member per day
    num_members = 150
    messages_per_day = 50

    # Calculate the number of messages sent by the removed members
    messages_removed = 20 * messages_per_day

    # Calculate the number of messages sent by the remaining members in a week
    messages_remaining_per_week = (num_members - 20) * messages_per_day * 7

    # Calculate the total number of messages sent in a week
    total_messages = messages_removed + messages_remaining_per_week

    # Display the total number of messages
    result = total_messages
    return result

print(solution())