def solution():
    """Willow’s daughter had a slumber party with 3 of her friends. For breakfast, they wanted pancakes. Willow’s pancake recipe makes 1 serving of 4 pancakes. Each of the girls wanted a serving and a half of pancakes. Willow’s son wanted 3 servings of pancakes. How many single pancakes will Willow make for the girls and her son?"""
    num_friends = 3
    pancakes_per_serving = 4
    pancakes_per_girl = 1.5 * pancakes_per_serving
    num_girls = num_friends
    num_son_servings = 3
    total_pancakes = (pancakes_per_girl * num_girls) + (pancakes_per_serving * num_son_servings)
    result = total_pancakes
    return result

print(solution())