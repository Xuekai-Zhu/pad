def solution():
    """Jerry takes 2 antacids that weigh 2 grams each and are 5% zinc by weight. Then he takes three more smaller antacids that weigh 1 gram each and have 15% zinc. How many milligrams of zinc does he eat?"""
    # Define the weight and zinc percentage of the first type of antacid
    weight1 = 2  # in grams
    zinc1 = 0.05  # as a decimal

    # Define the weight and zinc percentage of the second type of antacid
    weight2 = 1  # in grams
    zinc2 = 0.15  # as a decimal

    # Calculate the total weight of antacids consumed
    total_weight = weight1 * 2 + weight2 * 3  # in grams

    # Calculate the total amount of zinc consumed
    total_zinc = weight1 * zinc1 * 2 + weight2 * zinc2 * 3  # in grams

    # Convert the total zinc consumed to milligrams
    total_zinc_mg = total_zinc * 1000

    # Return the result
    result = total_zinc_mg
    return result

print(solution())