def solution():
    """The doctor told Barry to take vitamin D3 for 180 days to help protect him from infections. The pharmacy only sold vitamin D3 in bottles containing 60 capsules, with a daily serving size of 2 capsules.  How many bottles would Barry need to buy to have enough servings to last for 180 days?"""
    # Define the number of capsules per serving and per bottle
    CAPSULES_PER_SERVING = 2
    CAPSULES_PER_BOTTLE = 60

    # Calculate the number of servings needed for 180 days
    servings_needed = 180 / CAPSULES_PER_SERVING

    # Calculate the number of bottles needed
    bottles_needed = servings_needed / CAPSULES_PER_BOTTLE
    bottles_needed = round(bottles_needed + 0.5)

    # Display the number of bottles needed
    result = bottles_needed
    return result

print(solution())