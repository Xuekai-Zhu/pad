def solution():
    members_removed = 20
    messages_per_day = 50
    members_remaining = 150 - members_removed
    messages_per_week = messages_per_day * members_remaining * 7
    result = messages_per_week
    return result

print(solution())