def solution():
    """The owner of a small store divided the sugar into 12 packs. If each pack weighs 250 grams and has 20 grams of sugar left, how many grams of sugar did he start with?"""
    # Define the weight of sugar in each pack and the amount left in each pack.
    SUGAR_PER_PACK = 250
    SUGAR_LEFT_PER_PACK = 20

    # Calculate the total weight of sugar left in the packs.
    total_sugar_left = 12 * SUGAR_LEFT_PER_PACK

    # Calculate the weight of sugar originally in the packs.
    total_sugar = total_sugar_left + (12 * SUGAR_PER_PACK)

    # Display the total weight of sugar originally in the packs.
    result = total_sugar
    return result

print(solution())