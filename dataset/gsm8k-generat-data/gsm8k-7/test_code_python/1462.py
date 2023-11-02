def solution():
    num_lollipops = 100
    num_hard_candies = 5
    total_food_colouring = 600  # millilitres

    # Calculate total food colouring used in lollipops
    lollipop_food_colouring = num_lollipops * 5

    # Calculate total food colouring used in hard candies
    hard_candy_food_colouring = total_food_colouring - lollipop_food_colouring

    # Calculate how much food colouring each hard candy needs
    food_colouring_per_hard_candy = hard_candy_food_colouring / num_hard_candies

    result = food_colouring_per_hard_candy
    return result

print(solution())