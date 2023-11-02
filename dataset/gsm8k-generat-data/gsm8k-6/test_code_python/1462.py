def solution():
    # Calculate how much food colouring is used in making lollipops
    lollipop_coloring = 100 * 5

    # Calculate how much food coloring is used in making all candies
    total_coloring = lollipop_coloring + 5 * x

    # Calculate how much food coloring is left for hard candies
    hard_candy_coloring = 600 - total_coloring

    # Calculate how much food coloring each hard candy needs
    coloring_per_hard_candy = hard_candy_coloring / 5
    result = coloring_per_hard_candy
    return result

print(solution())