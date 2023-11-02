def solution():
    """Ashton had two boxes of pencils with fourteen pencils in each box. He gave six pencils to his brother. How many pencils did Ashton have left?"""
    pencils_per_box = 14
    total_pencils = pencils_per_box * 2
    pencils_given_away = 6
    pencils_left = total_pencils - pencils_given_away
    result = pencils_left
    return result

print(solution())