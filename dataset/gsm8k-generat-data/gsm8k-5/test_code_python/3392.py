def solution():
    total_paintings = 80  # Bethany saw a total of 80 paintings
    still_lifes = 4  # Bethany saw 4 times more still lifes than portraits

    # Calculate the number of still lifes Bethany saw
    still_lifes_count = total_paintings / (still_lifes + 1)

    # Calculate the number of portraits Bethany saw
    portraits_count = total_paintings - still_lifes_count

    result = portraits_count
    return result

print(solution())