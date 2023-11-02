def solution():
    total_spent = 37
    total_notebooks = 12
    num_red = 3
    red_price = 4
    num_green = 2
    green_price = 2

    # Find the total cost of red and green notebooks combined
    total_red_green_cost = (num_red * red_price) + (num_green * green_price)

    # Find the total number of blue notebooks
    num_blue = total_notebooks - num_red - num_green

    # Find the cost per blue notebook
    blue_price = (total_spent - total_red_green_cost) / num_blue
    result = blue_price
    return result

print(solution())