def solution():
    """A DVD can be played 1000 times before it breaks. There are two DVDs in the public library, one has been played 356 times and the other has been played 135 times. How many total times can both DVDs be played before they break?"""
    max_plays = 1000
    dvd1_plays = 356
    dvd2_plays = 135
    total_plays = dvd1_plays + dvd2_plays
    remaining_plays = 2 * max_plays - total_plays
    result = remaining_plays
    return result

print(solution())