def solution():
    # Calculate the cost of red and green notebooks
    cost_red = 3 * 4
    cost_green = 2 * 2

    # Calculate the total cost of blue notebooks
    total_cost_blue = 37 - cost_red - cost_green

    # Calculate the cost of each blue notebook
    cost_blue = total_cost_blue / 7  # 7 blue notebooks were bought since 3 red and 2 green were bought

    result = cost_blue
    return result

print(solution())