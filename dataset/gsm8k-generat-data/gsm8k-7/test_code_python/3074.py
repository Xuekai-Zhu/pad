def solution():
    num_green = 20
    num_red = 20
    num_yellow = 14

    # Calculate the new number of green M&Ms after Carter eats 12
    num_green -= 12

    # Calculate the new number of red M&Ms after Carter's sister eats half
    num_red /= 2

    # Calculate the total number of M&Ms remaining
    total_mms = num_green + num_red + num_yellow

    # Calculate the probability of picking a green M&M
    prob_green = num_green / total_mms

    # Convert the probability to a percentage
    percent_green = prob_green * 100
    result = percent_green
    return result

print(solution())