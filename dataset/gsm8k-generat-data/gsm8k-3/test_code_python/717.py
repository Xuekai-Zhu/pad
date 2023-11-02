def solution():
    """Jake splits 8 shots of vodka with his friend.  Each shot of vodka is 1.5 ounces.  If the vodka is 50% pure alcohol, how much pure alcohol did Jake drink?"""
    # Define the volume and purity of each shot of vodka
    SHOT_VOLUME = 1.5
    PURITY = 0.5

    # Calculate the total volume and pure alcohol consumed by Jake
    total_volume = 8 * SHOT_VOLUME
    pure_alcohol = total_volume * PURITY

    # Display the amount of pure alcohol consumed by Jake
    result = pure_alcohol
    return result

print(solution())