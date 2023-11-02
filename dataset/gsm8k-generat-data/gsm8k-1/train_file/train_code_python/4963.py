def solution():
    """After violating the group's policies, 20 members of a Facebook group were removed by the group's admin. If each member posted 50 messages per day in the group and the number of members in the group was 150 before the admin removed some, calculate the total number of messages the remaining members would send in a week."""
    members_before_removal = 150
    members_removed = 20
    members_remaining = members_before_removal - members_removed
    messages_per_day_per_member = 50
    days_in_a_week = 7
    total_messages = members_remaining * messages_per_day_per_member * days_in_a_week
    result = total_messages
    return result

print(solution())