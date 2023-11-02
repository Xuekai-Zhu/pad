def solution():
    """For 12 servings of Chicken Surprise, you need 4.5 pounds of chicken and 24 ounces of stuffing. How many ounces would one serving of Chicken Surprise be?"""
    # Define the amount of chicken and stuffing needed for 12 servings
    CHICKEN_PER_12 = 4.5 # pounds
    STUFFING_PER_12 = 24 # ounces

    # Calculate the amount of chicken and stuffing needed for one serving
    CHICKEN_PER_1 = CHICKEN_PER_12 / 12 # pounds
    STUFFING_PER_1 = STUFFING_PER_12 / 12 # ounces

    # Calculate the total amount of ounces for one serving
    total_ounces = (CHICKEN_PER_1 * 16) + STUFFING_PER_1 # convert pounds to ounces

    # Display the amount of ounces for one serving
    result = total_ounces
    return result

print(solution())