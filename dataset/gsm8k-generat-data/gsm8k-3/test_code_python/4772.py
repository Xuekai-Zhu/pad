def solution():
    """Vann is a veterinarian. Today he is going to be doing dental cleanings only. Dogs have 42 teeth, cats have 30 teeth and pigs have 28 teeth. If he is to do 5 dogs, 10 cats and 7 pigs, how many total teeth will Vann clean today?"""
    # Define the number of teeth for each type of animal
    DOG_TEETH = 42
    CAT_TEETH = 30
    PIG_TEETH = 28

    # Define the number of each animal Vann will be cleaning
    num_dogs = 5
    num_cats = 10
    num_pigs = 7

    # Calculate the total number of teeth Vann will clean
    total_teeth = (num_dogs * DOG_TEETH) + (num_cats * CAT_TEETH) + (num_pigs * PIG_TEETH)

    # Display the total number of teeth
    result = total_teeth
    return result

print(solution())