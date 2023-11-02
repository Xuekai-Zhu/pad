def solution():
    """Henry believes in the famous phrase, "An apple a day, keeps the doctor away." If a box contains 14 apples, how many weeks can Henry and his brother spend eating 3 boxes of apples if they each eat 1 apple a day?"""
    apples_per_box = 14
    weekly_apples_per_person = 7
    daily_apples_per_person = 1
    total_boxes = 3
    total_apples = apples_per_box * total_boxes
    weeks_of_apples = total_apples / (weekly_apples_per_person * daily_apples_per_person)
    result = weeks_of_apples
    return result

print(solution())