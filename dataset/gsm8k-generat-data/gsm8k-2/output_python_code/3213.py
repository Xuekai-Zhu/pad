def solution():
    """Carla had 400 chickens on her chicken farm. However, 40% of the chicken died due to a certain disease. How many chickens were there if she bought ten times as many chickens as the number that died due to disease?"""
    starting_chickens = 400
    disease_percentage = 0.4
    remaining_chickens = starting_chickens * (1 - disease_percentage)
    bought_chickens = 10 * (starting_chickens * disease_percentage)
    total_chickens = remaining_chickens + bought_chickens
    result = total_chickens
    return result

print(solution())