def solution():
    """Henry believes in the famous phrase, "An apple a day, keeps the doctor away." If a box contains 14 apples, how many weeks can Henry and his brother spend eating 3 boxes of apples if they each eat 1 apple a day?"""
    apples_per_box = 14
    apples_per_day = 2  # Henry and his brother will eat a total of 2 apples per day
    boxes_needed = (apples_per_day * 7) * 3 / apples_per_box
    result = boxes_needed / 2  # Divide by 2 because Henry and his brother are sharing the apples
    return result

print(solution())