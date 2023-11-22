def solution():
    
    total_stitches = 1800
    collar_stitches = total_stitches / 10
    rosette_stitches = collar_stitches * 2
    total_sleeves = 2
    stitches_per_sleeve = total_stitches - collar_stitches - rosette_stitches
    stitches_per_sleeve = stitches_per_sleeve / total_sleeves
    result = stitches_per_sleeve
    return result

print(solution())