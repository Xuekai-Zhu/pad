def solution():
    # Calculate the total number of hours left for Rita to swim
    total_hours = 1500 - (50 + 9 + 121)  # total hours left after completing backstroke, breaststroke and butterfly

    # Calculate the number of months needed to fulfill the coach's requirements
    months_needed = total_hours // 220  # assuming Rita practices 220 hours every month

    result = months_needed
    return result

print(solution())