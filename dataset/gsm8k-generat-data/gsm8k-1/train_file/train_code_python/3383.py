def solution():
    """ The doctor told Barry to take vitamin D3 for 180 days to help protect him from infections. The pharmacy only sold vitamin D3 in bottles containing 60 capsules, with a daily serving size of 2 capsules. How many bottles would Barry need to buy to have enough servings to last for 180 days?"""
    days = 180
    capsules_per_bottle = 60
    serving_size = 2
    servings_per_bottle = capsules_per_bottle / serving_size
    total_servings_needed = days * serving_size
    total_bottles_needed = total_servings_needed / servings_per_bottle
    result = total_bottles_needed
    return result

print(solution())