def solution():
    """Jeff has a shelter where he currently takes care of 20 cats. On Monday he found 2 kittens in a box and took them to the shelter. On Tuesday he found 1 more cat with a leg injury. On Wednesday 3 people adopted 2 cats each. How many cats does Jeff currently have in his shelter?"""
    # Define the initial number of cats
    initial_cats = 20

    # Add the cats that Jeff found on Monday
    monday_cats = 2
    total_cats = initial_cats + monday_cats

    # Add the cat that Jeff found on Tuesday
    tuesday_cats = 1
    total_cats += tuesday_cats

    # Subtract the cats that were adopted on Wednesday
    wednesday_cats = 3 * 2
    total_cats -= wednesday_cats

    # return the number of cats in Jeff's shelter
    result = total_cats
    return result

print(solution())