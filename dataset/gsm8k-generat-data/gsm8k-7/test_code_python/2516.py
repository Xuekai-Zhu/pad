def solution():
    num_red_balloons = 2
    num_blue_balloons = 4
    num_new_balloons = 4

    # Calculate the total number of balloons after inflating
    total_balloons = num_red_balloons + num_blue_balloons + num_new_balloons

    # Calculate the likelihood of selecting a red balloon
    likelihood_of_red = (num_red_balloons + 2) / total_balloons * 100
    result = likelihood_of_red
    return result

print(solution())