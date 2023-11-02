def solution():
    """Jake splits 8 shots of vodka with his friend. Each shot of vodka is 1.5 ounces. If the vodka is 50% pure alcohol, how much pure alcohol did Jake drink?"""
    # Define the volume of one shot in ounces and the percentage of pure alcohol in the vodka
    SHOT_VOLUME = 1.5
    PURE_ALCOHOL_PERCENTAGE = 0.5

    # Calculate the total volume of vodka consumed by Jake
    total_vodka_consumed = 8 * SHOT_VOLUME * 0.5

    # Calculate the volume of pure alcohol consumed by Jake
    pure_alcohol_consumed = total_vodka_consumed * PURE_ALCOHOL_PERCENTAGE

    # round off the result to 1 decimal place
    result = round(pure_alcohol_consumed, 1)
    return result

print(solution())