def solution():
    total_flowers = 40  # Ariana bought a bunch of 40 flowers
    roses = 2/5 * total_flowers  # 2/5th of the flowers bought were roses
    tulips = 10  # Ariana bought 10 tulips
    carnations = total_flowers - roses - tulips  # Calculate the number of carnations by subtracting roses and tulips from total flowers
    result = carnations
    return result

print(solution())