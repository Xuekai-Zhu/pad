def solution():
    # Calculate the number of green M&Ms left after Carter eats 12
    green_MMs_left = 20 - 12

    # Calculate the number of red M&Ms left after Carter's sister eats half and adds 14 yellow M&Ms
    red_MMs_left = (20/2) - 14

    # Calculate the total number of M&Ms left
    total_MMs_left = green_MMs_left + red_MMs_left + 14  # Carter's sister adds 14 yellow M&Ms

    # Calculate the probability of picking a green M&M
    probability_green_MM = (green_MMs_left / total_MMs_left) * 100
    result = probability_green_MM
    return result

print(solution())