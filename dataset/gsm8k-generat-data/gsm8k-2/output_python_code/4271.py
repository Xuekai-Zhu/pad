def solution():
    """For 12 servings of Chicken Surprise, you need 4.5 pounds of chicken and 24 ounces of stuffing. How many ounces would one serving of Chicken Surprise be?"""
    servings = 12
    chicken_weight = 4.5
    stuffing_weight = 24
    total_weight = chicken_weight + (stuffing_weight / 16)  # convert stuffing weight in ounces to pounds
    weight_per_serving = total_weight / servings
    ounces_per_serving = weight_per_serving * 16  # convert weight in pounds to ounces
    result = ounces_per_serving
    return result

print(solution())