def solution():
    """Anna wants to plant red and yellow tulips in the shape of a smiley face. She needs 8 red tulips for each eye and 18 red tulips for the smile. If she needs 9 times the number of tulips in the smile to make the yellow background of the face, how many tulips does she need total?"""
    red_tulips = 8 * 2 + 18
    yellow_tulips = 9 * 18
    total_tulips = red_tulips + yellow_tulips
    result = total_tulips
    return result

print(solution())