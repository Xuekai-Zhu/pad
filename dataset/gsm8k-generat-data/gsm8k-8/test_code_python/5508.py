def solution():
    # Calculate the total number of purple beads and their cost
    purple_beads = 50 * 20
    purple_cost = purple_beads / 10

    # Calculate the total number of blue beads and their cost
    blue_beads = 40 * 18
    blue_cost = blue_beads / 10

    # Calculate the total cost of all the beads
    total_cost = purple_cost + blue_cost + 80

    result = total_cost
    return result

print(solution())