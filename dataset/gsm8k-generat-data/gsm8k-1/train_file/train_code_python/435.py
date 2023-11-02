def solution():
    """Catherine had an equal number of pencils and pens. If she had 60 pens and gave eight pens and 6 pencils to each of her seven friends and kept the rest for herself, how many pens and pencils did she have left?"""
    pens = 60
    pencils = pens
    total_given = 8 * 7 + 6 * 7
    pens_given = 8 * 7
    pencils_given = 6 * 7
    pens_left = pens - pens_given
    pencils_left = pencils - pencils_given
    result = (pens_left, pencils_left)
    return result

print(solution())