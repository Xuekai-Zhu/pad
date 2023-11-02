def solution():
    """Jam has three boxes full of pencils and 2 loose pencils which give a total of 26 pencils. If her sister, Meg, has 46 pencils, how many boxes do Jam and Meg need to store all their pencils?"""
    jam_pencils = 26 - 2
    meg_pencils = 46
    pencils_per_box = 8
    total_pencils = jam_pencils + meg_pencils
    boxes_needed = total_pencils // pencils_per_box
    if total_pencils % pencils_per_box > 0:
        boxes_needed += 1
    result = boxes_needed
    
    return result

print(solution())