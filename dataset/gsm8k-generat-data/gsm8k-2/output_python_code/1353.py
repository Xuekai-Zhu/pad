def solution():
    """Archie needs to lay sod in his backyard that measures 20 yards by 13 yards. He has a shed on it that measures 3 yards by 5 yards. How many square yards of sod will Archie need for his backyard?"""
    backyard_area = 20 * 13
    shed_area = 3 * 5
    sod_needed = backyard_area - shed_area
    result = sod_needed
    return result

print(solution())