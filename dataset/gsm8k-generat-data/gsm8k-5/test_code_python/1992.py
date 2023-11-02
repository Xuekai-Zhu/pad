def solution():
    bubbles_per_ounce_dawn = 200000  # 1 ounce of Dawn can make 200,000 bubbles
    bubbles_per_ounce_bronner = 2 * bubbles_per_ounce_dawn  # Bronner can make twice as many bubbles per ounce as Dawn
    mixture_amount = 0.5  # We want to know the number of bubbles from a mixture of equal parts Dawn and Bronner

    # Calculate the total number of bubbles from the mixture
    total_bubbles = mixture_amount * ((0.5 * bubbles_per_ounce_dawn) + (0.5 * bubbles_per_ounce_bronner))

    result = total_bubbles
    return result

print(solution())