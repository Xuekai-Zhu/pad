def solution():
    """Willow’s daughter had a slumber party with 3 of her friends.  For breakfast, they wanted pancakes.  Willow’s pancake recipe makes 1 serving of 4 pancakes.  Each of the girls wanted a serving and a half of pancakes.  Willow’s son wanted 3 servings of pancakes.  How many single pancakes will Willow make for the girls and her son?"""
    # Define the number of servings of pancakes needed
    girls_servings = 4.5 # Each of the 3 girls wants 1.5 servings
    son_servings = 3

    # Calculate the total number of servings needed
    total_servings = girls_servings * 3 + son_servings

    # Calculate the total number of single pancakes needed
    total_pancakes = total_servings * 4

    # Display the total number of single pancakes needed
    result = total_pancakes
    return result

print(solution())