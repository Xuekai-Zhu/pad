def solution():
    jars_per_box1 = 12  # Cassy packs 12 jars of jam in 10 boxes
    boxes1 = 10
    jars_per_box2 = 10  # Cassy packs 10 jars of jam in 30 boxes
    boxes2 = 30
    total_jars = 500  # Cassy has 500 jars of jam

    # Calculate the total number of jars Cassy packs in all the boxes
    total_jars_packed = (jars_per_box1 * boxes1) + (jars_per_box2 * boxes2)

    # Calculate the number of jars left when all the boxes are full
    jars_left = total_jars - total_jars_packed
    result = jars_left
    return result

print(solution())