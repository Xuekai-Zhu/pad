def solution():
    """If 2 machines in a factory make 10 cell phones each minute, how many machines would it take to make 50 cell phones a minute?"""
    machines_needed = (50/10)/2
    result = machines_needed
    return result

print(solution())