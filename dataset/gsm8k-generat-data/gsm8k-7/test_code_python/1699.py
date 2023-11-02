def solution():
    num_orange = 10
    num_red = 2 * num_orange
    num_yellow = num_red - 5
    total_flowers = 105

    # Calculate the total number of orange, red, and yellow flowers
    total_orange_red_yellow = num_orange + num_red + num_yellow

    # Calculate the number of pink and purple flowers
    num_pink_purple = total_flowers - total_orange_red_yellow
    num_each_color = num_pink_purple / 2
    result = num_each_color
    return result

print(solution())