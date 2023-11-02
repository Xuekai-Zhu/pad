def solution():
    """Catherine had an equal number of pencils and pens. If she had 60 pens and gave eight pens and 6 pencils to each of her seven friends and kept the rest for herself, how many pens and pencils did she have left?"""
    total_pens = 60
    total_pencils = total_pens
    pens_given = 8 * 7
    pencils_given = 6 * 7
    remaining_pens = total_pens - pens_given
    remaining_pencils = total_pencils - pencils_given
    result = (remaining_pens, remaining_pencils)
    return result

print(solution())