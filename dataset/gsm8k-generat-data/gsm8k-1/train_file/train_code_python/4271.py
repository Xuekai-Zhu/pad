def solution():
    """For 12 servings of Chicken Surprise, you need 4.5 pounds of chicken and 24 ounces of stuffing. How many ounces would one serving of Chicken Surprise be?"""
    servings = 12
    chicken = 4.5 * 16  # convert pounds to ounces
    stuffing = 24
    total_weight = chicken + stuffing
    weight_per_serving = total_weight / servings
    result = weight_per_serving
    return result

print(solution())