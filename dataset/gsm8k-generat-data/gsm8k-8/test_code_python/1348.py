def solution():
    # Calculate the cost per cube of beef
    cost_per_cube = 25 / 80

    # Calculate the cost of 4 cubes, which is one kabob stick
    cost_per_kabob = cost_per_cube * 4

    # Calculate the total cost for 40 kabob sticks
    total_cost = cost_per_kabob * 40
    result = total_cost
    return result

print(solution())