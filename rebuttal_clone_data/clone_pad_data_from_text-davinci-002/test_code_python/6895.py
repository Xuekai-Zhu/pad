def solution():
    johns_dance_time = 3 + 5
    johns_break_time = 1
    james_dance_time = johns_dance_time + 1/3
    total_dance_time = johns_dance_time + james_dance_time
    result = total_dance_time - johns_break_time
    return result

print(solution())