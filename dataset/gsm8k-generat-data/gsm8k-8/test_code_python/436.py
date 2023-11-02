def solution():
    # Calculate the total number of pens and pencils
    total_items = 60 * 2

    # Calculate the total number of items given to friends
    items_given_away = 8 * 7 + 6 * 7

    # Calculate the remaining number of pens and pencils
    remaining_items = total_items - items_given_away

    # Calculate the number of pens and pencils left
    pens_left = remaining_items // 2
    pencils_left = pens_left

    result = (pens_left, pencils_left)
    return result

print(solution())