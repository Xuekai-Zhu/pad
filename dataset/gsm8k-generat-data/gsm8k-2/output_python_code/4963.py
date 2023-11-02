def solution():
    """After violating the group's policies, 20 members of a Facebook group were removed by the group's admin. If each member posted 50 messages per day in the group and the number of members in the group was 150 before the admin removed some, calculate the total number of messages the remaining members would send in a week."""
    remaining_members = 150 - 20
    messages_per_day = 50
    total_messages_in_week = remaining_members * messages_per_day * 7
    result = total_messages_in_week
    return result

print(solution())