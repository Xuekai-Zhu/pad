def solution():
    """A family bought a 24 pack of bottled water. They drank 1/3 of them on the first day and 1/2 of what was left after the first day on the second day. How many bottles of water remain after 2 days?"""
    total_bottles = 24
    first_day_percent = 1/3
    first_day_consumed = total_bottles * first_day_percent
    remaining_bottles = total_bottles - first_day_consumed
    second_day_percent = 1/2
    second_day_consumed = remaining_bottles * second_day_percent
    remaining_bottles -= second_day_consumed
    result = remaining_bottles
    return result

print(solution())