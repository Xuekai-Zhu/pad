def solution():
    """Carla, Kyle, and Tasha caught 36 fish. If Kyle and Tasha caught the same number of fish and Carla caught 8, how many fish did Kyle catch?"""
    # Determine the total number of fish caught by Kyle and Tasha combined
    total_kyle_tasha = 36 - 8

    # Divide the total number of fish by 2 to get the number caught by each of them (since they caught the same amount)
    kyle = total_kyle_tasha / 2

    result = kyle
    return result

print(solution())