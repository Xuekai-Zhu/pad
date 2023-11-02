def solution():
    """A family bought a 24 pack of bottled water. They drank 1/3 of them on the first day and 1/2 of what was left after the first day on the second day. How many bottles of water remain after 2 days?"""
    total_bottles = 24
    day1_consumed = total_bottles / 3
    day1_remaining = total_bottles - day1_consumed
    day2_consumed = day1_remaining / 2
    total_remaining = day1_remaining - day2_consumed
    result = total_remaining
    return result

print(solution())