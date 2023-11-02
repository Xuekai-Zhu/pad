def solution():
    points_needed = 2000
    chocolate_bunny_points = 8 * 100
    snickers_points = 25

    # Calculate the remaining points needed after selling the chocolate bunnies
    remaining_points = points_needed - chocolate_bunny_points

    # Calculate the number of Snickers bars needed to earn the remaining points
    num_snickers_needed = remaining_points / snickers_points
    result = num_snickers_needed
    return result

print(solution())