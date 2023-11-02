def solution():
    """Barkley gets 10 new dog bones at the beginning of the month. After 5 months, he has 8 bones available and has buried the rest. How many bones has he buried?"""
    starting_bones = 10
    remaining_bones = 8
    months_passed = 5
    buried_bones = (starting_bones - remaining_bones) * months_passed
    result = buried_bones
    return result

print(solution())