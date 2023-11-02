def solution():
    """A herring has 40 oz of fat, an eel 20 oz, and a pike 10 more oz of fat than an eel. If Ellianna cooked and served 40 fish of each type, calculate how many ounces of fat she served."""
    # Calculate the total ounces of fat in 40 herrings
    herring_fat = 40 * 40

    # Calculate the total ounces of fat in 40 eels
    eel_fat = 40 * 20

    # Calculate the fat in a pike
    pike_fat = eel_fat + 10

    # Calculate the total ounces of fat in 40 pikes
    pike_total_fat = 40 * pike_fat

    # Calculate the total ounces of fat in all the fish
    total_fat = herring_fat + eel_fat + pike_total_fat

    # Return the result
    result = total_fat
    return result

print(solution())