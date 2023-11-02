def solution():
    
    sweater_stitches = 900
    collar_stitches = sweater_stitches / 10
    rosette_stitches = collar_stitches * 2
    total_stitches = sweater_stitches + collar_stitches + rosette_stitches
    num_sleeves = 1800 // 2
    stitches_per_sleeve = total_stitches // num_sleeves
    result = stitches_per_sleeve
    return result

print(solution())