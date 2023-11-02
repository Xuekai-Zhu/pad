def solution():
    # Calculate the number of still lifes and portraits Bethany saw
    total_paintings = 80
    ratio = 4  # Bethany saw 4 times more still lifes than portraits
    total_ratio = ratio + 1  # total ratio of still lifes to portraits
    portraits = total_paintings / total_ratio
    result = portraits
    return result

print(solution())