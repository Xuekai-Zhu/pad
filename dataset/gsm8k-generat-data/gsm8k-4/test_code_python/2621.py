def solution():
    """In Fifi's closet, she hangs all of her clothes on colored plastic hangers. She has clothes hanging on 7 pink hangers, 4 green hangers, one less blue hanger than there are green hangers, and one less yellow hanger than there are blue hangers. What is the total number of colored hangers in Fifi's closet?"""
    # Calculate the number of blue hangers
    blue_hangers = 4 - 1

    # Calculate the number of yellow hangers
    yellow_hangers = blue_hangers - 1

    # Calculate the total number of colored hangers
    colored_hangers = 7 + 4 + blue_hangers + yellow_hangers

    # return the result
    result = colored_hangers
    return result

print(solution())