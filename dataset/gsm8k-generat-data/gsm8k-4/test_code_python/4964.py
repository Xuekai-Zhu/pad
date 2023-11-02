def solution():
    """After violating the group's policies, 20 members of a Facebook group were removed by the group's admin. If each member posted 50 messages per day in the group and the number of members in the group was 150 before the admin removed some, calculate the total number of messages the remaining members would send in a week."""
    # Define the initial number of group members and the number of members removed
    initial_members = 150
    removed_members = 20

    # Calculate the number of remaining members
    remaining_members = initial_members - removed_members

    # Calculate the total number of messages that the remaining members would send in a day
    messages_per_day = remaining_members * 50
    
    # Calculate the total number of messages that the remaining members would send in a week
    messages_per_week = messages_per_day * 7

    result = messages_per_week
    return result

print(solution())