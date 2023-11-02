def solution():
    """Cassy packs 12 jars of jam in 10 boxes while she packs 10 jars of jam in 30 boxes. If she has 500 jars of jams, how many jars of jam will she have left when all the boxes are full?"""
    jam_in_box1 = 12
    box1 = 10
    jam_in_box2 = 10
    box2 = 30
    total_jars = 500

    # Calculate the number of jars that can be packed using the first set of boxes
    boxes_needed1 = total_jars // (jam_in_box1 * box1)
    jars_packed1 = boxes_needed1 * jam_in_box1 * box1

    # Calculate the number of jars that can be packed using the second set of boxes
    boxes_needed2 = total_jars // (jam_in_box2 * box2)
    jars_packed2 = boxes_needed2 * jam_in_box2 * box2

    # Calculate the remaining jars after packing
    remaining_jars = total_jars - jars_packed1 - jars_packed2

    result = remaining_jars
    return result

print(solution())