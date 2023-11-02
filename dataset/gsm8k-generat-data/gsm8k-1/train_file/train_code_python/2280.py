def solution():
    """Willow’s daughter had a slumber party with 3 of her friends. For breakfast, they wanted pancakes. Willow’s pancake recipe makes 1 serving of 4 pancakes. Each of the girls wanted a serving and a half of pancakes. Willow’s son wanted 3 servings of pancakes. How many single pancakes will Willow make for the girls and her son?"""
    num_friends = 3
    servings_per_friend = 1.5
    num_servings_friends = num_friends * servings_per_friend
    num_servings_son = 3
    total_servings = num_servings_friends + num_servings_son
    pancakes_per_serving = 4
    total_pancakes = total_servings * pancakes_per_serving
    result = total_pancakes
    return result

print(solution())