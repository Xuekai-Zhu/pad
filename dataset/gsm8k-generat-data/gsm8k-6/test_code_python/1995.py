def solution():
    # Calculate the percentage reduction in photographs taken
    percentage_reduction = 20
    reduced_photos = 100 - (100 * percentage_reduction/100)  # 20% fewer photographs

    # Calculate the number of photographs needed to reach the target
    remaining_photos = 300 - reduced_photos
    result = remaining_photos
    return result

print(solution())