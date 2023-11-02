def solution():
    """In Fifi's closet, she hangs all of her clothes on colored plastic hangers. She has clothes hanging on 7 pink hangers, 4 green hangers, one less blue hanger than there are green hangers, and one less yellow hanger than there are blue hangers. What is the total number of colored hangers in Fifi's closet?"""
    pink_hangers = 7
    green_hangers = 4
    blue_hangers = green_hangers - 1
    yellow_hangers = blue_hangers - 1
    total_hangers = pink_hangers + green_hangers + blue_hangers + yellow_hangers
    result = total_hangers
    return result

print(solution())