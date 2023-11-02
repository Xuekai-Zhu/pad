def solution():
    """Jerry takes 2 antacids that weigh 2 grams each and are 5% zinc by weight. Then he takes three more smaller antacids that weigh 1 gram each and have 15% zinc. How many milligrams of zinc does he eat?"""
    # Define the weight and zinc percentage of the first type of antacid
    ANTACID1_WEIGHT = 2  # grams
    ANTACID1_ZINC_PERCENTAGE = 5  # %

    # Define the weight and zinc percentage of the second type of antacid
    ANTACID2_WEIGHT = 1  # gram
    ANTACID2_ZINC_PERCENTAGE = 15  # %

    # Calculate the total weight of the antacids Jerry takes
    total_weight = 2 * ANTACID1_WEIGHT + 3 * ANTACID2_WEIGHT  # grams

    # Calculate the total amount of zinc he consumes
    total_zinc = 2 * ANTACID1_WEIGHT * ANTACID1_ZINC_PERCENTAGE / 100 + 3 * ANTACID2_WEIGHT * ANTACID2_ZINC_PERCENTAGE / 100  # grams

    # Convert the total zinc to milligrams
    total_zinc_mg = total_zinc * 1000  # milligrams

    # Display the total amount of zinc Jerry consumes
    result = total_zinc_mg
    return result

print(solution())