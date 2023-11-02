def solution():
    """A cleaning company produces two sanitizer sprays. One spray kills 50% of germs, and another spray kills 25% of germs. However, 5% of the germs they kill are the same ones. What percentage of germs would be left after using both sanitizer sprays together?"""
    # Define the percentages of germs killed by each spray
    spray1_percent = 50
    spray2_percent = 25

    # Calculate the percentage of germs killed by both sprays
    both_sprays_percent = spray1_percent + (spray2_percent - (spray1_percent * spray2_percent) / 100)

    # Subtract the percentage of shared killed germs
    remaining_percent = both_sprays_percent - 5

    result = remaining_percent
    return result

print(solution())