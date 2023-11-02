def solution():
    # Calculate the total number of decorations Danai puts up
    total_decorations = 12 + 4 + 12 + 2*12 + 1  # 12 skulls, 4 broomsticks, 12 spiderwebs, 2x spiderwebs in pumpkins, 1 cauldron
    total_decorations += 20  # adding 20 more decorations
    total_decorations += 10  # adding 10 more decorations
    result = total_decorations
    return result

print(solution())