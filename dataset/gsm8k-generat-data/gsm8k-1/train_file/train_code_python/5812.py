def solution():
    """If 2 machines in a factory make 10 cell phones each minute, how many machines would it take to make 50 cell phones a minute?"""
    machines = 2
    phones_per_minute = 10
    target_phones_per_minute = 50
    machines_needed = target_phones_per_minute / phones_per_minute * machines
    result = machines_needed
    return result

print(solution())