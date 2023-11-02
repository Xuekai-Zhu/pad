def solution():
    # Calculate the total cost of the diamond earrings
    diamond_cost = 2 * 6000

    # Calculate the remaining cost after accounting for diamond earrings and iPhone
    remaining_cost = 20000 - diamond_cost - 2000

    # Calculate the number of scarves
    num_scarves = remaining_cost / 1500

    result = num_scarves
    return result

print(solution())