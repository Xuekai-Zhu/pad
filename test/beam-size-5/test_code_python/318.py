def solution():
    jam_boxes = 3
    jam_loose_pencils = 26
    meg_pencils = 46

    # Calculate the total number of pencils Jam and Meg have
    total_pencils = jam_pencils + meg_pencils - jam_loose_pencils

    # Calculate the number of boxes Jam and Meg need to store all their pencils
    total_boxes = total_pencils // 4
    result = total_boxes
    return result

print(solution())