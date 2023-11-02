def solution():
    # Calculate the total number of roses in the bouquet
    roses_in_bouquet = 3 * 12

    # Calculate the number of roses Susan gave to her daughter
    roses_given_to_daughter = roses_in_bouquet / 2

    # Calculate the number of roses left in the vase
    roses_in_vase = roses_in_bouquet - roses_given_to_daughter

    # Calculate the number of wilted flowers in the vase
    wilted_roses = roses_in_vase / 3

    # Calculate the number of roses remaining in the vase
    roses_remaining = roses_in_vase - wilted_roses
    result = roses_remaining
    return result

print(solution())