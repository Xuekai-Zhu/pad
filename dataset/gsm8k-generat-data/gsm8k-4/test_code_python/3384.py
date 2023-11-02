def solution():
    """The doctor told Barry to take vitamin D3 for 180 days to help protect him from infections. The pharmacy only sold vitamin D3 in bottles containing 60 capsules, with a daily serving size of 2 capsules. How many bottles would Barry need to buy to have enough servings to last for 180 days?"""
    # Define the number of days Barry needs to take vitamin D3
    days = 180

    # Define the number of capsules in a bottle and the daily serving size
    capsules_per_bottle = 60
    serving_size = 2

    # Calculate the total number of servings Barry needs
    total_servings = days * serving_size

    # Calculate the number of bottles Barry needs to buy, rounding up to the nearest integer
    bottles = int((total_servings + capsules_per_bottle - 1) / capsules_per_bottle)

    result = bottles
    return result

print(solution())