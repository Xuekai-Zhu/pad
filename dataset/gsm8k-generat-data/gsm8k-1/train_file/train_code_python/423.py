def solution():
    """Rose had 10 kilograms of rice. She cooked 9/10 kilograms in the morning and 1/4 of the remaining in the evening. How many grams of rice did she have left?"""
    starting_amount = 10000 #converted to grams
    morning_cooked = 9000
    remaining_after_morning = starting_amount - morning_cooked
    evening_cooked = remaining_after_morning / 4
    remaining_after_evening = remaining_after_morning - evening_cooked
    result = remaining_after_evening
    return result

print(solution())