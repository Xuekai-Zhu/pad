def solution():
    num_friends = 7
    pens = 60
    pencils = pens  # since Catherine had an equal number of pencils and pens

    # Calculate the total number of pens and pencils given out to friends
    total_pens_given = num_friends * 8
    total_pencils_given = num_friends * 6

    # Calculate the number of pens and pencils Catherine has left
    pens_left = pens - total_pens_given
    pencils_left = pencils - total_pencils_given

    result = (pens_left, pencils_left)
    return result

print(solution())