def solution():
    """Two sisters, Elizabeth and Margareth, bought beads. Elizabeth bought 1 pack of red and 2 packs of clear beads, while Margareth bought 3 packs of blue and 4 packs of red beads. How many more beads do one sister have than the other, if each pack of beads contains 20 pieces of beads?"""
    elizabeth_red = 1
    elizabeth_clear = 2
    margareth_red = 4
    margareth_blue = 3
    beads_per_pack = 20
    elizabeth_total = (elizabeth_red + elizabeth_clear) * beads_per_pack
    margareth_total = (margareth_red + margareth_blue) * beads_per_pack
    difference = abs(elizabeth_total - margareth_total)
    result = difference
    return result

print(solution())