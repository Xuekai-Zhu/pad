def solution():
    length_per_gift = 18
    inches_available = 90
    days_to_wrap = 3
    gifts_wrapped = (inches_available * days_to_wrap) / length_per_gift
    result = gifts_wrapped
    return result

print(solution())