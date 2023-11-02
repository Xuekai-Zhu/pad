def solution():
    """Barkley gets 10 new dog bones at the beginning of the month. After 5 months, he has 8 bones available and has buried the rest. How many bones has he buried?"""
    total_bones = 10 * 5
    available_bones = 8
    buried_bones = total_bones - available_bones
    result = buried_bones
    return result

print(solution())