def solution():
    # Calculate the total number of push-ups Geli will do in her first week
    push_ups_day1 = 10
    extra_push_ups = 5
    total_push_ups = push_ups_day1 + (extra_push_ups * 6)  # 6 days left in the first week
    result = total_push_ups
    return result

print(solution())