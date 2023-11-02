def solution():
    cherry_sours = 32
    lemon_ratio = 4/5
    orange_ratio = 0.25

    # Calculate the number of lemon sours
    lemon_sours = cherry_sours * lemon_ratio

    # Calculate the total weight of sours in the bag
    total_weight = cherry_sours + lemon_sours

    # Calculate the number of orange sours
    orange_sours = total_weight * orange_ratio

    # Calculate the total number of sours in the bag
    total_sours = cherry_sours + lemon_sours + orange_sours
    result = total_sours
    return result

print(solution())