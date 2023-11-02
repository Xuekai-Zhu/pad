def solution():
    """Anya washes 32 hairs down the drain when she washes her hair and brushes out half that amount when she brushes it. How many hairs does Anya have to grow back to always have one more hair than she started with after washing, brushing, and growing it?"""
    starting_hairs = 1
    hairs_washed = 32
    hairs_brushed = hairs_washed / 2
    hairs_grown_back = starting_hairs + hairs_washed + hairs_brushed - 1
    result = hairs_grown_back
    return result

print(solution())