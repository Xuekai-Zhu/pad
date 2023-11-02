def solution():
    balloons_on_string = 3 * 12  # 3 dozen balloons
    num_children = 3 + 12  # 3 boys and 12 girls

    # Calculate the total number of balloons bought by the children
    num_balloons_bought = num_children

    # Calculate the number of balloons still held by the clown
    num_balloons_left = balloons_on_string - num_balloons_bought
    result = num_balloons_left
    return result

print(solution())