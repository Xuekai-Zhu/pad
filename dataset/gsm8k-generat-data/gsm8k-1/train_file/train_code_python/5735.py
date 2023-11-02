def solution():
    """Ashton had two boxes of pencils with fourteen pencils in each box. He gave six pencils to his brother. How many pencils did Ashton have left?"""
    total_pencils = 2 * 14
    pencils_given = 6
    pencils_left = total_pencils - pencils_given
    result = pencils_left
    return result

print(solution())