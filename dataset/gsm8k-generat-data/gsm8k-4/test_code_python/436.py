def solution():
    """Catherine had an equal number of pencils and pens. If she had 60 pens and gave eight pens and 6 pencils to each of her seven friends and kept the rest for herself, how many pens and pencils did she have left?"""
    # Calculate the initial number of pencils and pens
    pens = 60
    pencils = pens

    # Calculate the total number of pens and pencils given to friends
    friend_pens = 8 * 7
    friend_pencils = 6 * 7
    total_given = friend_pens + friend_pencils

    # Subtract the total given from the initial number of pencils and pens
    pens_left = pens - friend_pens
    pencils_left = pencils - friend_pencils

    # Return the result
    result = (pens_left, pencils_left)
    return result

print(solution())