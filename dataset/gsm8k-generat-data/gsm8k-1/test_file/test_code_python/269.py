def solution():
    """Terri is knitting a sweater with two sleeves, a collar, and a decorative rosette. The body of the sweater takes 900 stitches to complete, the collar takes a tenth of that number of stitches, and the rosette takes twice as many as the collar. The whole sweater is an 1800-stitch project. How many stitches does each sleeve take?"""
    body_stitches = 900
    collar_stitches = body_stitches / 10
    rosette_stitches = collar_stitches * 2
    total_stitches = 1800
    sleeve_stitches = (total_stitches - body_stitches - collar_stitches - rosette_stitches) / 2
    result = sleeve_stitches
    return result

print(solution())