def solution():
    """There are 40 pupils in a class. Half of the class likes blue. One-fourth of the remaining likes green and the rest likes yellow. How many pupils like the color yellow?"""
    total_pupils = 40
    blue_likers = total_pupils / 2
    remaining_pupils = total_pupils - blue_likers
    green_likers = remaining_pupils / 4
    yellow_likers = remaining_pupils - green_likers
    result = yellow_likers
    return result

print(solution())