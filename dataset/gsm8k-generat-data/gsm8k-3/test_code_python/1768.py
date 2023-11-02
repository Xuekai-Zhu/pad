def solution():
    """Jeff has a shelter where he currently takes care of 20 cats. On Monday he found 2 kittens in a box and took them to the shelter. On Tuesday he found 1 more cat with a leg injury. On Wednesday 3 people adopted 2 cats each. How many cats does Jeff currently have in his shelter?"""
    # Define the initial number of cats in Jeff's shelter
    initial_cats = 20

    # Calculate the number of cats added on Monday
    monday_cats = 2

    # Calculate the number of cats added on Tuesday
    tuesday_cats = 1

    # Calculate the number of cats adopted on Wednesday
    wednesday_cats = 3 * 2

    # Calculate the total number of cats
    total_cats = initial_cats + monday_cats + tuesday_cats - wednesday_cats

    # Display the total number of cats
    result = total_cats
    return result

print(solution())