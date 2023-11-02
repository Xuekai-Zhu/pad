def solution():
    # Calculate the number of torn comics Aston has found
    torn_comics = 150 // 25  # each comic has 25 pages

    # Calculate the total number of comics in the box
    total_comics = torn_comics + 5  # adding torn comics to the 5 untorn comics already in the box
    result = total_comics
    return result

print(solution())