def solution():
    """It takes 320 rose petals to make an ounce of perfume. If each rose produces 8 petals, and there are 12 roses per bush, how many bushes will Fern have to harvest to make 20 12-ounce bottles of perfume?"""
    # Define the number of petals needed to make one 12-ounce bottle of perfume
    petals_per_bottle = 320 * 12

    # Calculate the number of petals needed to make 20 bottles
    total_petals = petals_per_bottle * 20

    # Calculate the number of roses needed to produce the required number of petals
    total_roses = total_petals / 8

    # Calculate the number of bushes needed to produce the required number of roses
    bushes = total_roses / 12

    # Round up to the nearest integer
    bushes = math.ceil(bushes)

    # return the result
    result = bushes
    return result

print(solution())