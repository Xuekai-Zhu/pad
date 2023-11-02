def solution():
    lollipop_coloring = 5  # 5 ml of food coloring is required for one lollipop
    hard_candy_coloring = (600 - (100 * lollipop_coloring)) / 5  # Total coloring used minus coloring used for lollipops, divided by number of hard candies

    result = hard_candy_coloring
    return result

print(solution())