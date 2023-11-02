def solution():
    num_machines = 2
    num_phones_per_minute = 10
    target_phones_per_minute = 50

    # Calculate the number of machines needed to produce the target number of phones per minute
    num_machines_needed = (num_machines * target_phones_per_minute) / num_phones_per_minute
    result = num_machines_needed
    return result

print(solution())