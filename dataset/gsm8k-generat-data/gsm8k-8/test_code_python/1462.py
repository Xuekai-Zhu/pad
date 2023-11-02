def solution():
    # Calculate the total amount of food colouring used for the lollipops
    lollipop_colouring = 100 * 5

    # Calculate the amount of food colouring used for the hard candies
    hard_candy_colouring = 600 - lollipop_colouring

    # Calculate how much food colouring each hard candy needs
    per_candy_colouring = hard_candy_colouring / 5
    result = per_candy_colouring
    return result

print(solution())