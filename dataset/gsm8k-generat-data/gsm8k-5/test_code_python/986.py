def solution():
    camden = 16  # Camden went swimming 16 times in March
    susannah = 24  # Susannah went swimming 24 times in March

    # Calculate the average number of times they went swimming per week
    avg_per_week = (camden + susannah) / 4

    # Calculate the difference in the number of times they went swimming per week
    difference = (susannah / 4) - (camden / 4)

    result = difference
    return result

print(solution())