def solution():
    """Willow’s daughter had a slumber party with 3 of her friends. For breakfast, they wanted pancakes. Willow’s pancake recipe makes 1 serving of 4 pancakes. Each of the girls wanted a serving and a half of pancakes. Willow’s son wanted 3 servings of pancakes. How many single pancakes will Willow make for the girls and her son?"""
    # Define the number of servings each person wants
    daughter_serve = 1.5
    friend_serve = 1.5
    son_serve = 3

    # Calculate the total number of servings needed
    total_serve = daughter_serve + (friend_serve * 3) + son_serve

    # Calculate the total number of pancakes needed
    total_pancakes = total_serve * 4

    result = total_pancakes
    return result

print(solution())