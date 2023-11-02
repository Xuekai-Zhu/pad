def solution():
    """Peggy fell off her bike and skinned her knees. She needed two bandages on her left knee and three bandages on her right knee. If the box of bandages had 8 less than two dozen bandages before Peggy skinned her knees, how many bandages were left in the box after Peggy finished putting bandages on her knees?"""
    left_knee_bandages = 2
    right_knee_bandages = 3
    total_bandages_used = left_knee_bandages + right_knee_bandages
    dozen_bandages = 24
    box_bandages = dozen_bandages - 8
    bandages_left = box_bandages - total_bandages_used
    result = bandages_left
    return result

print(solution())