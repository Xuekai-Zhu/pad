def solution():
    # Calculate the number of remaining members after 20 were removed
    remaining_members = 150 - 20

    # Calculate the total number of messages the remaining members would send in a day
    messages_per_day = remaining_members * 50

    # Calculate the total number of messages the remaining members would send in a week (7 days)
    messages_per_week = messages_per_day * 7
    result = messages_per_week
    return result

print(solution())