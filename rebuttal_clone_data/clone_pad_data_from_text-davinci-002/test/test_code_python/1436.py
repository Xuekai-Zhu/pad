def solution():
    reels_bought = 3
    length_per_reel = 100
    section_length = 10
    sections = reels_bought * (length_per_reel / section_length)
    result = sections
    return result

print(solution())