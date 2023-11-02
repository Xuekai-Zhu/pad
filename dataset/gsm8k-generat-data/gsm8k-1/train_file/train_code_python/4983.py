def solution():
    """Bill and Joan both work for a library. 5 years ago, Joan had 3 times as much experience as Bill. Now she has twice as much experience as Bill. How many years of experience does Bill have now?"""
    years_ago = 5
    ratio = 3
    years_since_ratio_changed = years_ago * 2
    years_of_experience_for_joan = years_since_ratio_changed + (years_ago * ratio)
    years_of_experience_for_bill = years_of_experience_for_joan / 2
    result = years_of_experience_for_bill
    return result

print(solution())