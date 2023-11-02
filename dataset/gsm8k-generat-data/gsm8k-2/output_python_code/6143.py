def solution():
    """20 kids in preschool are ready for a nap. 1/2 of the kids fall asleep within the first 5 minutes. Then half of the kids remaining fall asleep within another 5 minutes. How many kids are still awake?"""
    total_kids = 20
    first_wave = total_kids / 2
    second_wave = (total_kids - first_wave) / 2
    still_awake = total_kids - first_wave - second_wave
    result = still_awake
    return result

print(solution())