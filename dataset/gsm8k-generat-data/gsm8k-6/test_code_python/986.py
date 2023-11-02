def solution():
    # Calculate the average number of times they swam each week
    camden_swim = 16
    susannah_swim = 24
    total_swim = camden_swim + susannah_swim
    avg_swim = total_swim / 4

    # Calculate the difference in their weekly swimming
    diff = (susannah_swim / 4) - (camden_swim / 4)

    result = diff
    return result

print(solution())