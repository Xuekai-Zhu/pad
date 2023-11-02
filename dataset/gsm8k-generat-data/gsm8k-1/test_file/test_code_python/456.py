def solution():
    """Grayson recycles cans and bottles for money each week. An aluminum can is worth two cents and a plastic bottle is worth three cents. She drinks three aluminum cans of soda and five plastic bottles of water a week. How many cents does Grayson earn from recycling in a four-week month?"""
    cans_per_week = 3
    bottles_per_week = 5
    can_value = 2
    bottle_value = 3
    total_value = (cans_per_week * can_value + bottles_per_week * bottle_value) * 4
    result = total_value
    return result

print(solution())