def solution():
    total_flowers = 40
    roses_ratio = 2/5
    tulips = 10

    # Calculate the number of roses
    num_roses = total_flowers * roses_ratio

    # Calculate the number of carnations
    num_carnations = total_flowers - num_roses - tulips
    result = num_carnations
    return result

print(solution())