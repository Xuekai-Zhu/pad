def solution():
    # Find the total number of pencils and pens Catherine had
    total_items = 60 * 2  # since she had an equal number of pencils and pens

    # Find the total number of pencils and pens given away to her seven friends
    items_given_away = (8+6) * 7  # each friend receives 8 pens and 6 pencils

    # Find the number of pencils and pens left with Catherine
    items_left = total_items - items_given_away

    # Find the number of pens and pencils left with Catherine
    pens_left = items_left / 2
    pencils_left = items_left / 2

    result = (pens_left, pencils_left)
    return result

print(solution())