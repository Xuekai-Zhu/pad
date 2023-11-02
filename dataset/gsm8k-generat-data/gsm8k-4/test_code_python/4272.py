def solution():
    """For 12 servings of Chicken Surprise, you need 4.5 pounds of chicken and 24 ounces of stuffing. How many ounces would one serving of Chicken Surprise be?"""
    # Calculate the total amount of chicken and stuffing needed per serving
    chicken_per_serving = 4.5 / 12
    stuffing_per_serving = 24 / 12

    # Calculate the total amount of ounces per serving
    total_ounces_per_serving = (chicken_per_serving * 16) + stuffing_per_serving

    # Return the amount of ounces per serving
    result = total_ounces_per_serving
    return result

print(solution())