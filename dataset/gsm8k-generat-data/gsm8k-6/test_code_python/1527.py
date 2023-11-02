def solution():
    # Calculate the total number of balloons sold
    total_balloons_sold = 3 + 12  # 3 boys and 12 girls buy a balloon each
    total_balloons_on_string = 3 * 12  # 3 dozen (36) balloons on a string
    remaining_balloons = total_balloons_on_string - total_balloons_sold  # calculate the remaining balloons
    result = remaining_balloons
    return result

print(solution())