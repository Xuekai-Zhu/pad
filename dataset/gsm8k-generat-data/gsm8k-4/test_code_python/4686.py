def solution():
    """Darcy washes and drys 20 shirts and 8 pairs of shorts. If he folds 12 of the shirts and 5 of the shorts, how many more remaining pieces of clothing does Darcy have to fold?"""
    # Define the number of shirts and shorts that Darcy washes and drys
    num_shirts = 20
    num_shorts = 8 * 2

    # Define the number of shirts and shorts that Darcy folds
    num_folded_shirts = 12
    num_folded_shorts = 5

    # Calculate the number of remaining pieces of clothing that Darcy needs to fold
    remaining_shirts = num_shirts - num_folded_shirts
    remaining_shorts = num_shorts - num_folded_shorts
    remaining_clothes = remaining_shirts + remaining_shorts

    # return the result
    result = remaining_clothes
    return result

print(solution())