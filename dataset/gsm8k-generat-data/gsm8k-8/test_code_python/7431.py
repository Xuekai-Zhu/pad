def solution():
    # Calculate the total weight of fish
    total_weight = 8 + (6 * 2) + (2 * 12)

    # Divide the total weight by the amount of fish each person will eat
    num_campers = total_weight / 2

    result = num_campers
    return result

print(solution())