def solution():
    """To improve her health, Mary decides to drink 1.5 liters of water a day as recommended by her doctor. Mary's glasses hold 250 mL of water. How many glasses of water should Mary drink per day to reach her goal?"""
    # Define the recommended amount of water to drink in liters
    recommended_liters = 1.5

    # Convert the recommended amount to milliliters
    recommended_ml = recommended_liters * 1000

    # Calculate the number of glasses needed to reach the recommended amount of water
    glasses_per_day = recommended_ml / 250

    # Round up to the nearest integer
    result = int(glasses_per_day + 0.5)
    return result

print(solution())