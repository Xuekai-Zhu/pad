def solution():
    # Calculate the total number of purple and blue beads
    purple_beads = 50 * 20
    blue_beads = 40 * 18

    # Find the total number of beads used
    total_beads = purple_beads + blue_beads + 80

    # Calculate the total cost of the beads
    total_cost = (total_beads / 10) * 1

    result = total_cost
    return result

print(solution())