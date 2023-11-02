def solution():
    # Calculate the total amount of birdseed needed in grams
    total_birdseed = (2 * 7 * 3) + (14 * 7 * 2) + (1 * 2 * 7 * 4) / 2  
    # 2 grams a day for each parakeet for 7 days; 14 grams a day for each parrot for 7 days; 1 gram a day for each finch for 7 days divided by 2 because finches eat half of what a parakeet eats
    result = total_birdseed
    return result

print(solution())