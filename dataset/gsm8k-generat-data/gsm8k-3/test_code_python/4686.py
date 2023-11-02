def solution():
    """Darcy washes and drys 20 shirts and 8 pairs of shorts. If he folds 12 of the shirts and 5 of the shorts, how many more remaining pieces of clothing does Darcy have to fold?"""
    # Define the number of shirts and shorts washed and dried
    shirts = 20
    shorts = 8 * 2

    # Define the number of shirts and shorts folded
    shirts_folded = 12
    shorts_folded = 5 * 2

    # Calculate the remaining clothes to fold
    remaining_shirts = shirts - shirts_folded
    remaining_shorts = shorts - shorts_folded
    remaining_clothes = remaining_shirts + remaining_shorts

    # Display the remaining clothes to fold
    result = remaining_clothes
    return result

print(solution())