def solution():
    # Define the total number of balloons after inflating 4 more
    total_balloons = 2 + 4 + 4

    # Define the total number of red balloons after inflating 2 more
    total_red_balloons = 2 + 2

    # Calculate the percentage likelihood of selecting a red balloon
    percent_red_likelihood = (total_red_balloons / total_balloons) * 100
    result = percent_red_likelihood
    return result

print(solution())