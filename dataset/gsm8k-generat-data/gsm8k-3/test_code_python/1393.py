def solution():
    """Cassy packs 12 jars of jam in 10 boxes while she packs 10 jars of jam in 30 boxes. If she has 500 jars of jams, how many jars of jam will she have left when all the boxes are full?"""
    # Calculate the number of boxes needed for each type of jam
    boxes_12_jars = (500 // 12) // 10
    boxes_10_jars = (500 // 10) // 30

    # Determine the number of jars that fit in the boxes
    jars_in_boxes = (boxes_12_jars * 12 * 10) + (boxes_10_jars * 10 * 30)

    # Calculate the number of jars left
    jars_left = 500 - jars_in_boxes

    # Display the number of jars left
    result = jars_left
    return result

print(solution())