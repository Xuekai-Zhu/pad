def solution():
    # Define the number of rocks collected by Joshua and Jose
    joshua_rocks = 80
    jose_rocks = joshua_rocks - 14

    # Calculate the number of rocks collected by Albert
    albert_rocks = jose_rocks + 20

    # Calculate the difference between the number of rocks collected by Albert and Joshua
    difference = albert_rocks - joshua_rocks
    result = difference
    return result

print(solution())