def solution():
    # Calculate the distance covered by Abel in 0.7 hours
    distance_covered = 40 * 0.7  # Abel is driving at a speed of 40 miles per hour
    # Calculate the number of portions of the journey covered by Abel
    portions_covered = distance_covered / (35/5)  # 35 miles journey divided into 5 equal portions
    result = portions_covered
    return result

print(solution())