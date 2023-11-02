def solution():
    total_beads = 40
    num_amethysts = 7
    num_ambers = num_amethysts * 2

    # Calculate the total number of turquoise beads
    num_turquoises = total_beads - num_amethysts - num_ambers
    result = num_turquoises
    return result

print(solution())