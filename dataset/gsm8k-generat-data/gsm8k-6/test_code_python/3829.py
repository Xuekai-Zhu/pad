def solution():
    # Calculate the number of tangerines and oranges left in the bag
    oranges_left = 5 - 2  # 2 oranges were taken away
    tangerines_left = 17 - 10  # 10 tangerines were taken away

    # Calculate the difference in the number of tangerines and oranges left
    tangerines_more_than_oranges = tangerines_left - oranges_left
    result = tangerines_more_than_oranges
    return result

print(solution())